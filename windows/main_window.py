from windows.GUI import *
import windows.newFile_Dialog as file_dialog
import windows.project_dialog as project_dialog
import windows.mote_dialog as mote_dialog
import math
import os
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.timer import simulationTime
import traceback
import sys
from bs4 import BeautifulSoup
from classes.simulation import Simulation
import time as tempo5


class Edge(QGraphicsItem):

    def __init__(self, source, dest, size, color, parent=None):
        super().__init__(parent)

        self.removed = False
        self.parent = parent
        self.source = source
        self.dest = dest
        self.arrow = []
        self.arrowSize = size
        self.color = color
        if(self.color != Qt.red):
            self.fade()

    def boundingRect(self):
        p1 = self.source.boundingRect().center()
        p3 = self.dest.boundingRect().center()
        bounds = p3 - p1
        size = QSizeF(abs(bounds.x()), abs(bounds.y()))
        return QRectF(p1, size)

    def getArrow(self, line):
        angle = math.acos(line.dx() / line.length())
        if line.dy() >= 0:
            angle = (math.pi * 2.0) - angle
        return [
            line.p1(),
            line.p1() + QPointF(math.sin(angle + math.pi / 3.0) * self.arrowSize,
                                math.cos(angle + math.pi / 3.0) * self.arrowSize),
            line.p1() + QPointF(math.sin(angle + math.pi - math.pi / 3.0) * self.arrowSize,
                                math.cos(angle + math.pi - math.pi / 3.0) * self.arrowSize),
        ]

    def lines_point(self):
        x, y = self.source.getActualPosition()
        x1, y1 = self.dest.getActualPosition()
        return x, y, x1, y1

    def paint(self, painter, option, widget=None):
        painter.setRenderHint(QPainter.Antialiasing)
        coord = self.lines_point()

        painter.setPen(QtGui.QPen(self.color, 1))
        line = QLineF(coord[0], coord[1], coord[2], coord[3])
        line.setLength(line.length()-self.source.diameter/2)
        line = QLineF(line.x2(), line.y2(), line.x1(), line.y1())
        line.setLength(line.length()-self.source.diameter/2)
        painter.drawLine(line)
        poly = QPolygonF(self.getArrow(line))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawPolygon(poly)

    def fade(self):
        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

class Mote(QGraphicsItem):

    def __init__(self, position=(0, 0), title="1", diameter=25.0, parent=None):
        super().__init__(parent)

        self._title = title

        # Mote info
        self.x = position[0]
        self.y = position[1]
        self.diameter = diameter
        self.parent = None
        self.preferredParent = None
        self.egde = None
        self.parentList = []
        self.nextHop = None
        self.drawed = None

        # edge info
        self._pen_default = QPen(QColor("#7F000000"))
        self._pen_selected = QPen(QColor("#FFFFA637"))

        if(title == "1"):
            self._brush_background = QBrush(QColor("#B59BEE"))
        else:
            self._brush_background = QBrush(QColor("#B9B9B9"))

        self.initUI()

    def boundingRect(self):
        return QRectF(
            self.x,
            self.y,
            self.diameter,
            self.diameter
        ).normalized()

    def getTitle(self):
        return self._title

    def getParent(self):
        return self.parent

    def getPreferredParent(self):
        return self.preferredParent

    def setParent(self, parent, dest, color):
        self.parent = parent
        self.edge = Edge(self, dest, self.diameter/3, color)
        self.edge.setZValue(-1)
    
    def setPreferredParent(self, parent, dest):
        self.preferredParent = parent
        self.nextHop = Edge(self, dest, self.diameter/3, Qt.red)
        self.parentList.append(self.nextHop)
        self.nextHop.setZValue(-1)
    
    def removeEdge(self):
        self.parent = None
        self.edge = None

    def getEdge(self):
        return self.edge

    def getNextHop(self):
        return self.nextHop

    def getActualPosition(self):
        # rect = QRectF( self.scenePos().x(), self.scenePos().y(), self.diameter, self.diameter).normalized()
        rect = self.boundingRect()
        return [rect.center().x(), rect.center().y()]

    def getRadio(self):
        return self.diameter/2

    def initUI(self):
        pass

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):

        path_circle = QPainterPath()
        path_circle.setFillRule(Qt.WindingFill)
        path_circle.addEllipse(self.x, self.y, self.diameter, self.diameter)
        painter.setBrush(self._brush_background)
        painter.setPen(QtGui.QPen(Qt.black, 1))
        painter.drawPath(path_circle.simplified())

        painter.setPen(QtGui.QPen(Qt.black, 1))
        font = QtGui.QFont()
        font.setPointSize(10)
        painter.setFont(font)
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self._title)

    def changeColor(self, color):
        self._brush_background = QBrush(QColor(color))

    def scale(self, point):
        self.x = point[0]
        self.y = point[1]

    def fade(self):
        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()
        for parent in self.parentList:
            parent.fade()

class QDMGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        # settings
        self.gridSize = 20
        self.gridSquares = 5

        self._color_background = QColor("#FFFFFF")
        self._color_light = QColor("#F3F3F3")
        self._color_dark = QColor("#D9D9D9")

        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        self.scene_width, self.scene_height = 60000, 60000
        self.setSceneRect(-self.scene_width//2, -self.scene_height //
                          2, self.scene_width, self.scene_height)

        self.menu = QtWidgets.QMenu()
        self.selectedMote = ''
        self.motesInstance = None

        self.setBackgroundBrush(self._color_background)

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        # here we create our grid
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.gridSize)
        first_top = top - (top % self.gridSize)

        # compute all lines to be drawn
        lines_light, lines_dark = [], []
        for x in range(first_left, right, self.gridSize):
            if (x % (self.gridSize*self.gridSquares) != 0):
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.gridSize):
            if (y % (self.gridSize*self.gridSquares) != 0):
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_dark.append(QLine(left, y, right, y))

        if(lines_dark and lines_light):
            # draw the lines
            painter.setPen(self._pen_light)
            painter.drawLines(*lines_light)

            painter.setPen(self._pen_dark)
            painter.drawLines(*lines_dark)

    def setInstance(self, motes):
        self.motesInstance = motes

    def mousePressEvent(self, event):
        # Check it item exists on event position
        if event.button() == Qt.RightButton:
            point = QPointF(event.scenePos().toPoint())
            item = self.itemAt(point.x(),point.y(),  QtGui.QTransform())
            self.removeItem(self.menu.graphicsProxyWidget())
            self.defineMoteMenu()
            if item:
                # Try run items context if it has one
                try:
                    item.contextMenuEvent(event)
                    return
                except:
                    pass
                if isinstance(item, Mote):
                    self.selectedMote = item.getTitle()
                    self.addWidget(self.menu)
                    self.menu.exec_(point.toPoint())

    def defineMoteMenu(self):
        self.menu = QtWidgets.QMenu()
        self.showInfo = QAction(self)
        self.showInfo.setObjectName("Show mote info")
        self.showInfo.setText("Show mote info")
        self.showInfo.triggered.connect(self.openDialog)
        self.menu.addAction(self.showInfo)

    def openDialog(self):
        dialog = MoteDialog(self.motesInstance[self.selectedMote])
        if dialog.exec_():
            print('opened')
# Control Threads

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    '''
    finished = pyqtSignal()
    action = pyqtSignal(dict)
    logline = pyqtSignal(str)

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        if args:
            self.args[0].append(self.signals)
        else:
            self.args = [self.signals]

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        # try:
        self.fn(*self.args, **self.kwargs)
        # except:
        #     traceback.print_exc()
        #     exctype, value = sys.exc_info()[:2]
        #     self.signals.error.emit((exctype, value, traceback.format_exc()))
        # else:
        #     self.signals.result.emit(result)  # Return the result of the processing
        # finally:
        #     self.signals.finished.emit()

# Dialogs
class NewProjectDialog(QtWidgets.QDialog, file_dialog.Ui_Dialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.openlog.clicked.connect(self.openLog)
        self.openCsc.clicked.connect(self.openCSC)
        self.selected = {}

    def openLog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '', "(*.txt)", options=options)
        if fname[0] != '':
            self.selected['log'] = fname[0]
            self.log_name.setText(fname[0].split('/')[-1])

    def openCSC(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '', "(*.csc)", options=options)
        if fname[0] != '':
            self.selected['csc'] = fname[0]
            self.csc_name.setText(fname[0].split('/')[-1])

    def getSelection(self):
        self.selected['battery'] = str(int(self.Energy.text())*1000)
        self.selected['scale'] = self.scale.text()
        self.selected['diameter'] = self.width.text()
        self.selected['delay'] = self.delay.text().replace(',', '.')
        return self.selected

class NewProjectDialog(QtWidgets.QDialog, file_dialog.Ui_Dialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.openlog.clicked.connect(self.openLog)
        self.openCsc.clicked.connect(self.openCSC)
        self.selected = {}

    def openLog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '', "(*.txt)", options=options)
        if fname[0] != '':
            self.selected['log'] = fname[0]
            self.log_name.setText(fname[0].split('/')[-1])

    def openCSC(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '', "(*.csc)", options=options)
        if fname[0] != '':
            self.selected['csc'] = fname[0]
            self.csc_name.setText(fname[0].split('/')[-1])

    def getSelection(self):
        self.selected['battery'] = self.Energy.text()
        self.selected['scale'] = self.scale.text()
        self.selected['diameter'] = self.width.text()
        self.selected['delay'] = self.delay.text().replace(',', '.')
        return self.selected
 
class ProjectConfigDialog(QtWidgets.QDialog, project_dialog.Ui_Dialog):

    def __init__(self, energy, delay, width, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.energy.setValue(int(energy))
        self.delay.setValue(float(delay))
        self.width.setValue(int(width))

    def getParameters(self):
        return self.energy.value(), self.delay.value(), self.width.value()
        
class MoteDialog(QtWidgets.QDialog, mote_dialog.Ui_Dialog):

    def __init__(self, mote, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.mote = mote
        self.setupUi(self)  
        self.model = QStandardItemModel(self.information)
        self.label.setText(self.label.text() + ' ' + mote.getID())
        self.information.setModel(self.model)
        self.energy.clicked.connect(self.showTrace)
        self.parents.clicked.connect(self.showParentList)
        self.general.clicked.connect(self.showGeneral)
    
    def showTrace(self):
        self.model.clear()
        self.addLine('------------Energy trace----------')
        for energy in self.mote.getEnergyTrace():
            self.addLine(energy)

    def showParentList(self):
        self.model.clear()
        self.addLine('----------Preferred parents----------')
        parents = self.mote.getParents()
        for i in range(len(parents)):
            self.addLine(f'{self.mote.getTime(i)}:\tMote ID:{parents[i]}')

    def showGeneral(self):
        self.model.clear()
        self.addLine('-----------General Info-----------')
        self.addLine(f'Mote ID:                    {self.mote.getID()}')
        self.addLine(f'Mote type:                  Tmote Sky')
        self.addLine(f'Mote energy (mJ):           {self.mote.getBattery()}')
        self.addLine(f'Parent changes:             {self.mote.parentsChange() if self.mote.parentsChange() >= 0 else "No join"}')
        self.addLine(f'Average latency (segs):  {round(self.mote.getAverageLatency(), 3)}')

    def addLine(self, line):
        item = QStandardItem(line)
        item.setEditable(False)
        self.model.appendRow(item)

# Main Window

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.scene = QDMGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.drawn_motes = {}
        self.time = simulationTime(self.changeTime)
        self.edgeColors = list(filter(lambda color: 'dark' in color, QColor.colorNames()))

        # simulations state
        self.pauseLog = False
        self.startRead = False
        self.treeView = False

        # viewer zoom
        self.zoomInFactor = 1.15
        self.zoomClamp = False
        self.zoom = 1
        self.zoomStep = 1
        self.zoomRange = [0, 10]

        # QThreads control
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" %
              self.threadpool.maxThreadCount())

        # Events
        self.open.triggered.connect(self.fileChoose)
        self.save.triggered.connect(self.saveProject)
        self.dodag.triggered.connect(self._save_image)
        self.new_project.triggered.connect(self.newProject)
        self.parameters.triggered.connect(self.modifyParameters)
        self.topology.triggered.connect(self.showTopology)
        self.restart.triggered.connect(self.resetSimulation)
        self.cooja.triggered.connect(self.openCooja)
        self.run.clicked.connect(self.startTimer)
        self.reload.clicked.connect(self.resetSimulation)
        self.pause.clicked.connect(self.pauseTimer)


        # QtWidgets
        self.addZoomButtons()

    # Window events
    def resizeEvent(self, event):

        self.added.move(self.width() - 330, self.height() - 130)
        self.less.move(self.width() - 330, self.height() - 90)
        QtWidgets.QMainWindow.resizeEvent(self, event)

    # Menu actions
    def fileChoose(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', '', "(*.vtrc)", options=options)
        if fname[0] != '':
            with open(fname[0]) as file:
                soup = BeautifulSoup(file,  "lxml")
                self.simulation_parameters = {
                    'log': soup.log.getText(),
                    # 'sniffer': url + soup.sniffer.getText() + '.csv',
                    'csc': soup.csc_file.getText(),
                    'battery': soup.energylevel.getText(),
                    'scale': soup.node_scale.getText(),
                    'diameter': soup.mote_size.getText(),
                    'delay': soup.delay.getText(),
                    'path': fname[0]
                }
                self.getDODAG(self.simulation_parameters)
                self.scene.items().clear()
                self.scene.update()
                self.log.clear()
                self.optionState(True)

    def newProject(self):
        dialog = NewProjectDialog(self)
        if dialog.exec_():
            selection = dialog.getSelection()
            self.simulation_parameters = selection
            self.getDODAG(self.simulation_parameters)
            self.optionState(True)

    def saveProject(self):
        if not 'path' in self.simulation_parameters.keys():
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(
                self, "QFileDialog.getSaveFileName()", "", "All Files (*);", options=options)
            if fileName:
                f = open(fileName + ".vtrc", "w+")
                f.write(self.getWSP())
                f.close()
        else:
            f = open(self.simulation_parameters['path'], "w+")
            f.write(self.getWSP())
            f.close()

    def getWSP(self):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
    <simconfig>
        <simsfiles>
            <log>{self.simulation_parameters['log']}</log>
            <csc_file>{self.simulation_parameters['csc']}</csc_file>
        </simsfiles>
    <parameters> 
        <energylevel>{self.simulation_parameters['battery']}</energylevel>
        <delay>{self.simulation_parameters['delay']}</delay>
        <mote_size>{self.simulation_parameters['diameter']}</mote_size>
        <node_scale>{self.simulation_parameters['scale']}</node_scale>
    </parameters>
</simconfig>
        """

    def _save_image(self):

        self.scaleDODAG(3)
        area = QRectF(round(self.topologyArea['x1']*3,2)-50,round(self.topologyArea['y1']*3-50,2),round(abs(self.topologyArea['x2']-self.topologyArea['x1'])*3,2)+100, round(abs(self.topologyArea['y2']-self.topologyArea['y1'])*3,2)+100)
        # Create a QImage to render to and fix up a QPainter for it.
        image = QImage(area.size().toSize(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(image)

        # Render the region of interest to the QImage.
        self.scene.render(painter, target=QRectF(image.rect()), source=area)
        painter.end()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
                self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.png)", options=options)
        if fileName:
            image.save(fileName + ".png")

    def modifyParameters(self):
        dialog = ProjectConfigDialog(self.simulation_parameters['battery'], self.simulation_parameters['delay'], self.simulation_parameters['diameter'], parent=self)
        if dialog.exec_():
            e,d,w = dialog.getParameters()
            resetflag = 0
            if(e != self.simulation_parameters['battery']):
                self.simulation_parameters['battery'] = e
                resetflag = 1
            if(d != self.simulation_parameters['delay']):
                self.simulation_parameters['delay'] = d
                resetflag = 1
            if(w != self.simulation_parameters['diameter']):
                self.simulation_parameters['diameter'] = w
                resetflag = 1
            
            if(resetflag):
                self.resetSimulation()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setText("The simulation parameters has been updated.")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

    def showTopology(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("The simulation steps cannot be seen in the DODAG view. Do you want continue?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        val = msg.exec_()
        if(val == QMessageBox.Ok):
            self.cleanScene()
            self.log.clear()
            self.timer.setText("DODAG Phases View")
            self.trees = self.Sim.getDODAGTrace()
            self.drawDODAG(self.trees['00'],'00')
            #self.trees['00'].update( self.trees['01'])
            self.treeView = True
            self.run.setEnabled(False)
            self.pause.setEnabled(False)
            self.reload.setEnabled(False)
            self.parameters.setEnabled(False)
            self.save.setEnabled(False)
            self.Latency.setEnabled(False)
            self.Energy_consumption.setEnabled(False)
            self.DODAG_build.setEnabled(False)
            self.Control_messages.setEnabled(False)
            times = list(self.trees.keys())
            times.sort()
            for time in times:
                self.log.appendPlainText('DODAG tree at time -> ' + time + ':00')

        #self.log.clicked[QModelIndex].connect(self.selectTopology)

    def selectTopology(self, index):
        tree_in_time = self.model.itemFromIndex(index).text()[-5:-3]
        self.cleanScene()
        actual_tree = self.trees['00'].copy()
        actual_tree.update(self.trees[tree_in_time])
        self.drawDODAG(actual_tree, tree_in_time)
    
    def drawDODAG(self, topology, actualTime):
        self.Sim.sortDODAG(topology,actualTime)
        self.drawn_motes['1'] = Mote(self.Sim.getMotes()['1'].getDODAGPos(int(self.simulation_parameters['scale'])), '1', diameter=float(self.simulation_parameters['diameter']))
        self.scene.addItem(self.drawn_motes['1'])
        for mote in topology:
            if self.Sim.getMotes()[mote].diedAt !=  None:
                if(self.Sim.getMotes()[mote].diedAt > int(actualTime)):
                    self.drawn_motes[mote] = Mote(self.Sim.getMotes()[mote].getDODAGPos(int(self.simulation_parameters['scale'])), mote, diameter=float(self.simulation_parameters['diameter']))
                    self.drawn_motes[mote].setToolTip('Parent changes-->' + str(topology[mote]['changes']))
                    self.scene.addItem(self.drawn_motes[mote])
            else:
                self.drawn_motes[mote] = Mote(self.Sim.getMotes()[mote].getDODAGPos(int(self.simulation_parameters['scale'])), mote, diameter=float(self.simulation_parameters['diameter']))
                self.drawn_motes[mote].setToolTip('Parent changes-->' + str(topology[mote]['changes']))
                self.scene.addItem(self.drawn_motes[mote]) 

        for mote in self.drawn_motes:
            if (mote != '1'):
                if (self.Sim.getMotes()[topology[mote]['parent']].diedAt != None):
                    if (self.Sim.getMotes()[topology[mote]['parent']].diedAt > int(actualTime)):
                        self.drawn_motes[mote].setParent( topology[mote]['parent'], self.drawn_motes[topology[mote]['parent']], Qt.red)
                        self.scene.addItem(self.drawn_motes[mote].getEdge())
                else:
                    self.drawn_motes[mote].setParent( topology[mote]['parent'], self.drawn_motes[topology[mote]['parent']], Qt.red)
                    self.scene.addItem(self.drawn_motes[mote].getEdge())

    def openCooja(self):
        if os.name == 'nt':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Your System is not Linux Based you can't install Contiki directly, can you downloaded from official repositories.")
            msg.setStandardButtons(QMessageBox.Ok)
            val = msg.exec_()
        else:
            if(subprocess.check_output('[ -d "~/cooja/tools" ] || [ -d "~/contiki/tools/cooja" ] && echo "YES" || echo "NO"', shell=True) == "b'YES\\n'"):
                os.system('cd ~/contiki/tools/cooja\n ant run')
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Cooja is not instaled in your computer, download the sources files or install Instant Contiki instead.")
                msg.setStandardButtons(QMessageBox.Ok)
                val = msg.exec_()
    
    def optionState(self, state):
        self.run.setEnabled(state)
        self.pause.setEnabled(state)
        self.reload.setEnabled(state)
        self.log.setEnabled(state)
        self.parameters.setEnabled(state)
        self.menuRPL_Tree.setEnabled(state)
        self.save.setEnabled(state)
        self.dodag.setEnabled(state)
        self.dodag.setEnabled(state)
        self.Energy_consumption.setEnabled(state)
        self.Energy_consumption.setChecked(state)
        self.DODAG_build.setChecked(state)
        self.DODAG_build.setEnabled(state)
        self.Latency.setChecked(state)
        self.Latency.setEnabled(state)
        self.Control_messages.setEnabled(state)
        self.Control_messages.setChecked(state)
        self.added.setEnabled(state)
        self.less.setEnabled(state)
        self.zoom = 1
        self.zoomInFactor = 1.15
        self.treeView = False
        self.graphicsView.resetTransform()

    # Simulation Control
    def isPause(self):
        return self.pauseLog

    def runningInstance(self):
        return self.startRead

    def startTimer(self):
        if not self.startRead:
            self.startRead = True
            # Any other args, kwargs are passed to the run function
            workerFile = Worker(self.Sim.readLog, [
                                self.isPause, self.delay, self.runningInstance])
            workerFile.signals.logline.connect(self.changeTime)
            workerFile.signals.action.connect(self.controlLog)
            self.threadpool.start(workerFile)
        else:
            self.pauseLog = False

    def pauseTimer(self):
        self.pauseLog = not self.pauseLog

    def changeTime(self, time):
        self.timer.setText(time)

    def resetSimulation(self):
        self.getDODAG(self.simulation_parameters)
        self.scene.items().clear()
        self.scene.update()
        self.log.clear()
        self.optionState(True)
        # if("DODAG" in self.timer.text()):
        #     self.log.clicked[QModelIndex].disconnect()
        self.timer.setText("00:00.000")
    # Log control
    def controlLog(self, action):
        self.addLine(self.logAction(action))

    def logAction(self, action):
        if(action['action'] == 'energy' and self.Energy_consumption.isChecked()):
            if(action['energy_report'] > 70.0):
                self.drawn_motes[action['mote']].changeColor('#78DA04')
            elif (action['energy_report'] > 0.0):
                self.drawn_motes[action['mote']].changeColor('#FBFF00')
            else:
                self.drawn_motes[action['mote']].changeColor('#F5470F')
                self.drawn_motes[action['mote']].fade()
            self.scene.update()
            return f'{action["time"]}\tID:{action["mote"]}\tRemaining energy := {action["energy_report"]} %'
        elif(action['action'] == 'sendData' and self.Latency.isChecked()):
            if(action["parent"] != None):
                edge_color = QtGui.QColor()
                edge_color.setNamedColor(self.edgeColors[self.Sim.getMotes()[action["mote"]].parentListSize()-1])
                self.drawn_motes[action["mote"]].setParent( action["parent"], self.drawn_motes[action["parent"]], edge_color)
                self.scene.addItem(self.drawn_motes[action["mote"]].getEdge())
            return f'{action["time"]}\tID:{action["mote"]}\tSend DATA to sink'
        elif(action['action'] == 'receiveData' and self.Latency.isChecked()):
            return f'{action["time"]}\tID:{action["mote"]}\tRecieve DATA from mote {action["sender"]} in {action["segs"]} seconds'
        elif(action['action'] == 'buildDODAG' and self.DODAG_build.isChecked()):
            if(self.drawn_motes[action["mote"]].getPreferredParent() != action["parent"]):
                self.drawn_motes[action["mote"]].setPreferredParent( action["parent"], self.drawn_motes[action["parent"]])
                self.scene.addItem(self.drawn_motes[action["mote"]].getNextHop())
            return f'{action["time"]}\tID:{action["mote"]}\tBest parent selected: mote {action["parent"]}'

    def addLine(self, line):
        if line:
            self.log.appendPlainText(line)


    # Zoom Manager
    def addZoomButtons(self):
        plus = QtWidgets.QPushButton(self)
        plus.setGeometry(QtCore.QRect(580, 460, 35, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        plus.setFont(font)
        plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        plus.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/plus.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        plus.setIcon(icon)
        plus.setObjectName("plus")
        plus.setEnabled(False)
        plus.clicked.connect(self.zoomPlus)

        minus = QtWidgets.QPushButton(self)
        minus.setGeometry(QtCore.QRect(580, 500, 35, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        minus.setFont(font)
        minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        minus.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/minus.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        minus.setIcon(icon1)
        minus.setObjectName("minus")
        minus.setEnabled(False)
        minus.clicked.connect(self.zoomMinus)

        self.added = plus
        self.less = minus
        self.proxy = QtWidgets.QGraphicsProxyWidget()
        self.proxy.setWidget(plus)
        self.proxy.setWidget(minus)
        self.scene.addItem(self.proxy)

    def zoomPlus(self):
        # calculate our zoom Factor
        zoomOutFactor = 1 / self.zoomInFactor

        # calculate zoom
        zoomFactor = self.zoomInFactor
        self.zoom += self.zoomStep

        # set scene scale
        self.graphicsView.scale(zoomFactor, zoomFactor)
        self.scaleDODAG(self.zoom)

    def zoomMinus(self):
        # calculate our zoom Factor
        zoomOutFactor = 1 / self.zoomInFactor

        # calculate zoom
        zoomFactor = zoomOutFactor
        self.zoom -= self.zoomStep

        # set scene scale
        self.graphicsView.scale(zoomFactor, zoomFactor)
        self.scaleDODAG(self.zoom)

    # Simulation class
    def getDODAG(self, simulation):
        self.startRead = False
        self.delay = float(simulation['delay'])
        self.Sim = Simulation(
            simulation['log'], simulation['csc'], BateryEnergy=int(simulation['battery']))
        self.cleanScene()
        self.setBoundsArea()
        for mote in self.Sim.getMotes().values():
            self.defineArea(mote.getPosition(1))
            self.drawn_motes[mote.getID()] = Mote(mote.getPosition(int(simulation['scale'])), mote.getID(), diameter=float(simulation['diameter']))
            # self.drawn_motes[mote.getID()].setFlag(QGraphicsItem.ItemIsMovable)
            self.scene.addItem(self.drawn_motes[mote.getID()])
        self.scene.setInstance(self.Sim.getMotes())
        self.timer.setText("00:00.000")
        self.pauseLog = False

    def cleanScene(self):
        if(len(self.drawn_motes.keys()) != 0):
            self.scene.clear()
            self.scene.update()
            self.drawn_motes = {}

    def scaleDODAG(self, factor):
        for mote in self.drawn_motes.keys():
            if not self.treeView:
                self.drawn_motes[mote].scale(
                    self.Sim.getMotes()[mote].getPosition(int(self.simulation_parameters['scale']) + (factor-1)))
            else:
                self.drawn_motes[mote].scale(
                    self.Sim.getMotes()[mote].getDODAGPos(int(self.simulation_parameters['scale']) + (factor-1)))

    def defineArea(self, pos):
        if(pos[0] < self.topologyArea['x1']):
            self.topologyArea['x1'] = pos[0]
        elif(pos[0] > self.topologyArea['x2']):
            self.topologyArea['x2'] = pos[0]
            
        if(pos[1] < self.topologyArea['y1']):
            self.topologyArea['y1'] = pos[1]
        elif(pos[1] > self.topologyArea['y2']):
            self.topologyArea['y2'] = pos[1]

    def setBoundsArea(self):
        self.topologyArea = {
            'x1': 10000,
            'x2': -10000,
            'y1': 100000,
            'y2': -10000
        }


def run():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
