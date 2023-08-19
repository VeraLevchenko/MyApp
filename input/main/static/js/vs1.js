const form = document.getElementById('form');
function getFormValue(event) {
        event.preventDefault();
        const search_value = form.querySelector('[name="q"]');
        const result = search_value.value
        console.log('Результат:', result);
//        document.getElementById("qqq").innerHTML = result
    }
form.addEventListener('submit', getFormValue);
