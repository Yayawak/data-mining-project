document.getElementById('submitButton').addEventListener('click', function() {
    let fileInput = document.getElementById('csvFileInput');
    let file = fileInput.files[0];
    let reader = new FileReader();

    reader.onload = function(event) {
        let csvData = event.target.result;
        let rows = csvData.split(/\r?\n|\r/);
        let dataDisplay = document.getElementById('dataDisplay');

        dataDisplay.innerHTML = '';

        rows.forEach((row, index) => {
            if (index === 0) return;

            let cells = row.split(",");
            cells.forEach((cell, cellIndex) => {
                if (cell.trim() !== '') {
                    let columnName = rows[0].split(",")[cellIndex].trim();
                    let h1Element = document.createElement("h1");
                    h1Element.textContent = `${columnName} : ${cell.trim()}`;
                    dataDisplay.appendChild(h1Element);
                }
            });
        });
    };

    reader.readAsText(file);
});