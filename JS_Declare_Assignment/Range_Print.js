

function printRange(rangeStart, rangeStop) {
    var text = "";
        for (var i = rangeStart; i < rangeStop; i++) {
            text += i + ',';
        }
    return text;
    var result = text;
}
console.log(printRange(20, 30))
