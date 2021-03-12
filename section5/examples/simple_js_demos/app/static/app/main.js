// current_email = undefined;

document.addEventListener('DOMContentLoaded', function() {

    load_main();

    document.querySelector('#main').addEventListener('click', () => load_main());
    document.querySelector('#cars').addEventListener('click', () => load_cars());

    // document.querySelector('#reply').addEventListener('click', () => reply());
    // document.querySelector('#archive').addEventListener('click', () => archive(true));
    // document.querySelector('#unarchive').addEventListener('click', () => archive(false));

});


// function reply(){
//     alert(current_email);
// }


function load_main(){
    document.querySelector('#main-view').style.display = 'block';
    document.querySelector('#cars-view').style.display = 'none';
}


function load_cars(){
    document.querySelector('#main-view').style.display = 'none';
    document.querySelector('#cars-view').style.display = 'block';

    document.querySelector('#cars-view').innerHTML = 'This is cars view'

    fetch(`/cars`)
    .then(response => response.json())
    .then(cars => {
      if (cars.length === 0) {
        document.querySelector('#cars-view').innerHTML += 'No cars found.';
      }
      cars.forEach(add_car_to_view);
    });
    
}

function add_car_to_view(car){

    // Create a new element for the email
    const row = document.createElement('div');
    
    row.classList.add('car-entry');

    if (car.make === 'Lexus') {
        row.classList.add('lexus');
    }
    
    row.innerHTML = `<strong>${car.make}</strong> ${car.model} <span class='car-year'>${car.year}</span>`;

    // On car click
    row.addEventListener('click', function() {
        //show_car(car.id);
        alert(car.model);
    });

    // Add row to the view
    document.querySelector('#cars-view').append(row);

}


function show_car (id){
    // hide everythin but the single car view 1 block 2 none

    // fetch from `cars/${id}`

    // query selector and plug the values  of car.make , car.model


}