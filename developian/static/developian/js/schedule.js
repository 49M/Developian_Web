// let isDragging = false;
// let highlightedElements = [];
// let preHighlightedElem = null;

// document.addEventListener('DOMContentLoaded', function() {
//     const scheduleEvents = document.querySelectorAll('.schedule-event');

//     scheduleEvents.forEach(event => {
//         event.addEventListener('mousedown', function() {
//             isDragging = true;
//             toggleHighlight(event);
//         });

//         event.addEventListener('mousemove', function() {
//             if (isDragging) {
//                 toggleHighlight(event);
//             }
//         });
//     });
//     document.addEventListener('mouseup', function() {
//         isDragging = false;
//     });
// });
// function toggleHighlight(event) {
//     if (highlightedElements.includes(event)) {
//         highlightedElements.splice(highlightedElements.indexOf(event), 1);
//         event.classList.remove('highlighted');
//     } else {
//         preHighlightedElem = event;
//         if (preHighlightedElem != null) {
//             highlightedElements.push(preHighlightedElem);
//             preHighlightedElem.classList.add('highlighted');
//         }
//     }
// }
let isDragging = false;
let startElement = null;

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
    });
});

function highlightRange(start, end) {
    const scheduleEvents = Array.from(document.querySelectorAll('.schedule-event'));
    const startIndex = scheduleEvents.indexOf(start);
    const endIndex = scheduleEvents.indexOf(end);

    // Clear previous highlights
    // scheduleEvents.forEach(event => event.classList.remove('highlighted'));

    // Determine the range to highlight
    const [from, to] = startIndex < endIndex ? [startIndex, endIndex] : [endIndex, startIndex];
    for (let i = from; i <= to; i++) {
        scheduleEvents[i].classList.add('highlighted');
    }
}