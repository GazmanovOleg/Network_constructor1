const dragAndDrop = () => {
    const elem = document.querySelector('.js-elem');
    const field = document.querySelector('.js-field')

    const dragStart = function(){
        var newelem = elem.cloneNode(true);
        document.querySelector("div.img_container").appendChild(newelem);
    };
    const dragOver = function (evt){
        evt.preventDefault();

    };
    const dragEnter = function (evt){
        evt.preventDefault();
        this.classList.add('hovered');

    };
    const dragLeave = function (){
        this.classList.remove('hovered');

    };
    const dragDrop = function (){
       
        this.append(elem);
        this.classList.remove('hovered');

    };
    elem.addEventListener('dragstart',dragStart);
    field.addEventListener('dragover',dragOver);
    field.addEventListener('dragenter',dragEnter);
    field.addEventListener('dragleave',dragLeave);
    field.addEventListener('drop',dragDrop);
    
    
}
dragAndDrop();