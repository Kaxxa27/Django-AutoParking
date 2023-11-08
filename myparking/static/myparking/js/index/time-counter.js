// Получаем элемент с обратным отсчетом
const timeCounter = document.getElementById('time-counter');
const time = 60 * 60 * 1000; // 1 hour

// Функция для обратного отсчета
function startTimeCounter(targetTime) {
    const updateTimeCounter = () => {
         if (targetTime > 0) {
            const date = new Date(targetTime);
            const hours = date.getUTCHours();
            const minutes = date.getUTCMinutes();
            const seconds = date.getUTCSeconds();
            targetTime -= 1000;
            timeCounter.innerHTML = `Time Counter: ${hours}h ${minutes}m ${seconds}s`;
        } else {
            timeCounter.innerHTML = 'Timer is over!';
        }
    };

    updateTimeCounter();

    // Обновляем отсчет каждую секунду
    const timeCounterInterval = setInterval(updateTimeCounter, 1000);

    // Сохраняем состояние отсчета в локальное хранилище
    localStorage.setItem('timeCounterTargetTime', targetTime);

    // Очищаем интервал при завершении
    if (targetTime <= 0) {
        clearInterval(timeCounterInterval);
    }
} 

// Получаем целевое время из локального хранилища
const storedTargetTime = localStorage.getItem('timeCounterTargetTime');

if (storedTargetTime) {
    startTimeCounter(parseInt(storedTargetTime));
} else {
    const targetTime = time; 
    startTimeCounter(targetTime);
}
