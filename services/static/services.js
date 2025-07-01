document.addEventListener('DOMContentLoaded', () => {
	const cards = document.querySelectorAll('.serviceCard');
	const cardsPerPage = 2;
	const total = Math.ceil(cards.length / cardsPerPage);

	createCarouselDots(total);
});

let currentPage = 0;
let totalPages = 0;
let cardWidth = 0;

function scrollServices(direction) {
	const container = document.querySelector('.servicesContainer');
	const cards = container.querySelectorAll('.serviceCard');
	if (!container || cards.length === 0) return;

	const containerWidth = container.clientWidth;
	const style = getComputedStyle(container);
	const gap = parseFloat(style.gap) || 0;
	cardWidth = cards[0].offsetWidth + gap;

	const cardsPerPage = Math.floor(containerWidth / cardWidth) || 1;
	totalPages = Math.ceil(cards.length / cardsPerPage);
	const scrollAmount = cardWidth * cardsPerPage;

	// Update page index
	if (direction === 'right') {
		currentPage = currentPage + 1 >= totalPages ? 0 : currentPage + 1;
	} else {
		currentPage = currentPage - 1 < 0 ? totalPages - 1 : currentPage - 1;
	}

	const newScroll = scrollAmount * currentPage;
	container.scrollTo({ left: newScroll, behavior: 'smooth' });

	updateActiveDot(currentPage);
}

function createCarouselDots(numPages) {
	const dotsContainer = document.querySelector('.carouselDots');
	dotsContainer.innerHTML = '';

	for (let i = 0; i < numPages; i++) {
		const dot = document.createElement('span');
		dot.classList.add('dot');
		dot.dataset.page = i;
		if (i === 0) dot.classList.add('active');
		dotsContainer.appendChild(dot);
	}
}

function updateActiveDot(index) {
	const dots = document.querySelectorAll('.carouselDots .dot');
	dots.forEach((dot) => dot.classList.remove('active'));
	if (dots[index]) dots[index].classList.add('active');
}

document.addEventListener('DOMContentLoaded', () => {
	const container = document.querySelector('.servicesContainer');
	const cards = container.querySelectorAll('.serviceCard');

	const containerWidth = container.clientWidth;
	const gap = parseFloat(getComputedStyle(container).gap) || 0;
	const cardWidth = cards[0].offsetWidth + gap;
	const cardsPerPage = Math.floor(containerWidth / cardWidth) || 1;
	const total = Math.ceil(cards.length / cardsPerPage);

	createCarouselDots(total);
});

window.addEventListener('resize', () => {
	currentPage = 0; // reset to first page
	document.dispatchEvent(new Event('DOMContentLoaded')); // re-run dot setup
});

function updateJewelryForPiercing(element) {
	const title = element.getAttribute('data-service-title');
	const serviceId = element.getAttribute('data-service-id');

	console.log('Service Title:', title);
	console.log('Service ID:', serviceId);

	document.getElementById('jewelryContainerTitle').innerHTML = `${title} Jewelry`;

	fetch(`/piercings/detail/${serviceId}`)
		.then((response) => response.json())
		.then((data) => {
			if (data.error) {
				alert('Service not found');
				return;
			}

			// Find the container where jewelry information will be shown
			const modal = document.querySelector('#allJewelryContainer');

			modal.innerHTML = '';

			// Loop through all the jewelry items returned from the server
			data.forEach((jewelry) => {
				// Create a new div for each jewelry item (or use any other structure you need)
				const jewelryElement = document.createElement('div');
				jewelryElement.classList.add('jewelryItem');

				// Add jewelry details to the new div
				jewelryElement.innerHTML = `
                <img class="image" src="${jewelry.image}" alt="${jewelry.name}">

                <div class="jewelryItemDetailNameHeader">
                <h3 class="name">${jewelry.name}</h3>
                <div class="jewelryItemDetail">
                
                <p class="price">$${jewelry.price}</p>
                <p class="material">${jewelry.material}</p>
                </div>
                
                </div>
            `;

				// Append the jewelry element to the modal container
				modal.appendChild(jewelryElement);
			});
		})
		.catch((error) => {
			console.error('Error fetching data:', error);
			alert('There was an error loading the service details.');
		});
}
