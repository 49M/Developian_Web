let isDragging = false;
let startElement = null;
const scheduleEvents = Array.from(document.querySelectorAll('.schedule-event'));
let highlightedEvents = [];

document.addEventListener('DOMContentLoaded', function() {
    const scheduleEvents = document.querySelectorAll('.schedule-event');

    scheduleEvents.forEach(event => {
        event.addEventListener('mousedown', function() {
            isDragging = true;
            startElement = event;
            highlightRange(startElement, event);
        });

        event.addEventListener('mousemove', function() {
            if (isDragging) {
                highlightRange(startElement, event);
            }
        });
    });

    // Add mouseup event listener to the document
    document.addEventListener('mouseup', function() {
        isDragging = false;
        startElement = null;
        finalizeHighlight();
    });
});

function highlightRange(start, end) {
    const startIndex = scheduleEvents.indexOf(start);
    const endIndex = scheduleEvents.indexOf(end);

    // Determine the range to highlight
    const [from, to] = startIndex < endIndex ? [startIndex, endIndex] : [endIndex, startIndex];

    scheduleEvents.forEach((event, index) => {
        if (index >= from && index <= to && !highlightedEvents.includes(event)) {
            event.classList.add('highlighted');
        } else if (!highlightedEvents.includes(event)) {
            event.classList.remove('highlighted');
        }
    });
}
function finalizeHighlight() {
    for (let i = 0; i < scheduleEvents.length; i++) {
        if (scheduleEvents[i].classList.contains('highlighted') && !highlightedEvents.includes(scheduleEvents[i])) {
            highlightedEvents.push(scheduleEvents[i]);
        }
    }
}