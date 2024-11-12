// Car details (similar to Python dictionary)
const carDetails = {
    'family cars': {
        'Ertiga': { 'Price': '₹8.64 lakh', 'Model': 'ZXI', 'Engine': '1.5L Petrol', 'Mileage': '19.01 kmpl', 'Seating': '7-seater' },
        'Kia Carens': { 'Price': '₹9.60 lakh', 'Model': 'Prestige', 'Engine': '1.5L Petrol', 'Mileage': '16.5 kmpl', 'Seating': '7-seater' },
        'Tata Nexon': { 'Price': '₹7.99 lakh', 'Model': 'XZ+', 'Engine': '1.2L Petrol', 'Mileage': '17.57 kmpl', 'Seating': '5-seater' }
    },
    'off roading cars': {
        'Mahindra Thar': { 'Price': '₹13.49 lakh', 'Model': 'LX', 'Engine': '2.0L Petrol', 'Mileage': '15.2 kmpl', 'Seating': '4-seater' },
        'Jimny': { 'Price': '₹12.74 lakh', 'Model': 'Zeta', 'Engine': '1.5L Petrol', 'Mileage': '16.94 kmpl', 'Seating': '4-seater' },
        'Urban Cruiser': { 'Price': '₹9.02 lakh', 'Model': 'Premium', 'Engine': '1.5L Petrol', 'Mileage': '17.03 kmpl', 'Seating': '5-seater' }
    },
    // Other categories can be added similarly
};

// Function to display car options based on the selected type
function getCarOptions() {
    const carType = document.getElementById('carType').value;
    const carList = document.getElementById('carList');
    carList.innerHTML = '';

    if (carType && carDetails[carType]) {
        let cars = Object.keys(carDetails[carType]);
        let html = `<h3>Available ${carType}</h3><ul>`;
        cars.forEach(car => {
            html += `<li><button onclick="showCarDetails('${carType}', '${car}')">${car}</button></li>`;
        });
        html += '</ul>';
        carList.innerHTML = html;
    } else {
        carList.innerHTML = '<p>Please select a valid car type.</p>';
    }
}

// Function to display car details
function showCarDetails(carType, car) {
    const carInfo = carDetails[carType][car];
    const carDetailsDiv = document.getElementById('carDetails');
    carDetailsDiv.innerHTML = `<h3>${car} Details</h3>`;
    for (let detail in carInfo) {
        carDetailsDiv.innerHTML += `<p><strong>${detail}:</strong> ${carInfo[detail]}</p>`;
    }

    // Show EMI section
    document.getElementById('emiSection').style.display = 'block';
}

// EMI calculation function
function calculateEMI() {
    const rate = document.getElementById('rate').value;
    const years = document.getElementById('years').value;
    const carType = document.getElementById('carType').value;
    const car = document.getElementById('carDetails').getElementsByTagName('h3')[0].innerText.split(' ')[0];

    const priceString = carDetails[carType][car]['Price'];
    const price = parseFloat(priceString.replace('₹', '').replace(' lakh', '').replace(',', '')) * 100000;

    const monthlyRate = rate / (12 * 100);
    const emi = price * monthlyRate * Math.pow((1 + monthlyRate), (years * 12)) / (Math.pow((1 + monthlyRate), (years * 12)) - 1);

    document.getElementById('emiResult').innerHTML = `<p>EMI for ${car} is approximately ₹${emi.toFixed(2)} per month.</p>`;
}

// Function to exit the app
function exitApp() {
    alert("Thank you for visiting our showroom! Have a great day! 👋");
    window.location.reload();
}
