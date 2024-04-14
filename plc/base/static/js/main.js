
console.log('Раньше было лучше')

popup = document.getElementById('popup')
buttonOpenPopup = document.getElementById('openPopup')
buttonClosePopup = document.getElementById('closePopup')


buttonOpenPopup.addEventListener('click', () => {
    popup.style.display = 'block'
    document.getElementById('blurWrapper').style.filter='blur(5px)';
})
buttonClosePopup.addEventListener('click', () => {
    popup.style.display = 'none'
    document.getElementById('blurWrapper').style.filter='none';
})