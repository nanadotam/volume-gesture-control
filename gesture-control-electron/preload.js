const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('api', {
  startGestureControl: () => ipcRenderer.send('start-gesture-control'),
  stopGestureControl: () => ipcRenderer.send('stop-gesture-control'),
  onVolumeUpdate: (callback) => ipcRenderer.on('update-volume', callback),
})
