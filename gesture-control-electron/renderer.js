const startButton = document.getElementById('start-button')
const stopButton = document.getElementById('stop-button')
const volumeDisplay = document.getElementById('volume-display')

startButton.addEventListener('click', () => {
  window.api.startGestureControl()
  startButton.disabled = true
  stopButton.disabled = false
})

stopButton.addEventListener('click', () => {
  window.api.stopGestureControl()
  startButton.disabled = false
  stopButton.disabled = true
})

window.api.onVolumeUpdate((event, volume) => {
  volumeDisplay.textContent = `Volume: ${volume}%`
})
