# -*- coding: utf-8 -*-

from . import mapboxgl
from qgis.PyQt.QtWidgets import QAction, QFileDialog

import sys
sys.path.append('/Applications/PyCharm.app/Contents/debug-eggs/pycharm-debug.egg')
import pydevd
pydevd.settrace('localhost', port=53100, stdoutToServer=True, stderrToServer=True)

class MapboxGLPlugin:

    def __init__(self, iface):
        self.iface = iface

    def unload(self):
        self.iface.removePluginMenu(u"Mapbox GL", self.actionImport)
        self.iface.removePluginMenu(u"Mapbox GL", self.actionExport)
        self.iface.removePluginMenu(u"Mapbox GL", self.actionExportWithApp)

    def initGui(self):
        self.actionImport = QAction("Import Mapbox GL...", self.iface.mainWindow())
        self.actionImport.triggered.connect(self.importMapbox)
        self.iface.addPluginToMenu(u"Mapbox GL", self.actionImport)
        self.actionExport = QAction("Export Mapbox GL...", self.iface.mainWindow())
        self.actionExport.triggered.connect(lambda: self.exportMapbox(False))
        self.iface.addPluginToMenu(u"Mapbox GL", self.actionExport)
        self.actionExportWithApp = QAction("Export Mapbox GL (include test OL app)...", self.iface.mainWindow())
        self.actionExportWithApp.triggered.connect(lambda: self.exportMapbox(True))
        self.iface.addPluginToMenu(u"Mapbox GL", self.actionExportWithApp)        


    def importMapbox(self):
        filename = QFileDialog.getOpenFileName(self.iface.mainWindow(), 'Open Mapbox File')
        if filename:
            mapboxgl.openProjectFromMapboxFile(filename)
        
    def exportMapbox(self, includeApp):
        folder =  QFileDialog.getExistingDirectory(self.iface.mainWindow(), "Select folder to store project",
                                                        "", QFileDialog.ShowDirsOnly)
        if folder:
            mapboxgl.projectToMapbox(folder, includeApp)
    