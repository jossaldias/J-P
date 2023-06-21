function printTableContent() {
    var table = document.querySelector('table');
    var columnIndexToRemove = 6;
    var clonedTable = table.cloneNode(true);
    var rows = clonedTable.getElementsByTagName('tr');
    for (var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName('td');
        if (cells.length > columnIndexToRemove) {
            cells[columnIndexToRemove].remove();
        }
    }

    var tableContent = clonedTable.innerHTML;
    var printWindow = window.open('', '', 'width=600,height=400');
    printWindow.document.open();
    printWindow.document.write('<html><head><title>Informe</title>');
    printWindow.document.write('<style>table, tr, td { border: 1px solid black; border-collapse: collapse; }</style>');
    printWindow.document.write('</head><body>');
    printWindow.document.write('<table>');
    printWindow.document.write(tableContent);
    printWindow.document.write('</table>');
    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.print();
    printWindow.close();

}

document.querySelectorAll('.printbutton').forEach(function (element) {
    element.addEventListener('click', printTableContent);
});


function printTableContentInv() {
    var tableContent = document.querySelector('tableinventario').innerHTML;
    var printWindow = window.open('', '', 'width=600,height=400');
    printWindow.document.open();
    printWindow.document.write('<html><head><title>Contenido de la tabla</title>');
    printWindow.document.write('<style>table, tr, td { border: 1px solid black; border-collapse: collapse; }</style>');
    printWindow.document.write('</head><body>');
    printWindow.document.write('<table>');
    printWindow.document.write(tableContent);
    printWindow.document.write('</table>');
    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.print();
    printWindow.close();

}

document.querySelectorAll('.printbuttoninv').forEach(function (element) {
    element.addEventListener('click', printTableContent);
});



function imprimirOrden(elemento) {
    var ventana = window.open('', 'PRINT', 'height=400,width=600');
    ventana.document.write('<html><head><title>' + document.title + '</title>');
    ventana.document.write('</head><body >');
    ventana.document.write(elemento.innerHTML);
    ventana.document.write('</body></html>');
    ventana.document.close();

    var elementosNoImprimir = ventana.document.querySelectorAll('.no-print');
    elementosNoImprimir.forEach(function (elemento) {
        elemento.style.display = 'none';
    });
    ventana.focus();
    ventana.print();
    ventana.close();
    return true;
}

document.querySelector("#btnImprimir").addEventListener("click", function () {
    var div = document.querySelector("#imprimible");
    imprimirOrden(div);
});
