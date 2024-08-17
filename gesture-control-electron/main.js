const { app, BrowserWindow, ipcMain } = require('electron')
const path = require('path')
const { spawn } = require('child_process')

let pythonProcess
let mainWindow

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      enableRemoteModule: false,
      nodeIntegration: false,
    },
  })

  mainWindow.loadFile('index.html')
}

ipcMain.on('start-gesture-control', () => {
  pythonProcess = spawn('python3', ['gesture_control.py'])

  pythonProcess.stdout.on('data', (data) => {
    const volume = data.toString().trim()
    mainWindow.webContents.send('update-volume', volume)
  })

  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`)
  })

  pythonProcess.on('close', (code) => {
    console.log(`Python script exited with code ${code}`)
  })
})

ipcMain.on('stop-gesture-control', () => {
  if (pythonProcess) {
    pythonProcess.kill()
  }
})

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) createWindow()
})
