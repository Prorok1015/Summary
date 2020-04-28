searchBox1 = document.querySelector("#searchBox1");
searchBox2 = document.querySelector("#searchBox2");



function search(e) {
    let text = e.target.value; 
    if (e.target == searchBox1)
    {
        countries = document.querySelector("#id_category");
    }else if (e.target == searchBox2){
        countries = document.querySelector("#id_Site");
    }
    let options = countries.options; 
    for (let i = 0; i < options.length; i++) {
        let option = options[i]; 
        let optionText = option.text; 
        let lowerOptionText = optionText.toLowerCase();
        let lowerText = text.toLowerCase(); 
        let regex = new RegExp("^" + text, "i");
        let match = optionText.match(regex); 
        let contains = lowerOptionText.indexOf(lowerText) != -1;
        if (match || contains) {
            option.selected = true;
            return;
        }
        searchBox1.selectedIndex = 0;
    }
}
searchBox1.addEventListener("keyup", search);
searchBox2.addEventListener("keyup", search);
