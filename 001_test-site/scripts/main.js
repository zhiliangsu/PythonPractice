let myImage = document.querySelector('img');
let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');

function setUserName() {
    let myName = prompt('请输入你的名字。');
    if (!myName || myName === null) {
        setUserName();
    } else {
        localStorage.setItem('name', myName);
        myHeading.textContent = 'Mozilla 酷毙了，' + myName;
    }
}

if (!localStorage.getItem('name')) {
    setUserName();
} else {
    let stored_name = localStorage.getItem('name');
    myHeading.textContent = 'Mozilla 酷毙了，' + stored_name;
}

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    alert(mySrc);
    if (mySrc === 'images/firefox.png') {
        myImage.setAttribute('src', 'images/firefox2.png');
    } else {
        myImage.setAttribute('src', 'images/firefox.png');
    }
}

myButton.onclick = function() {
    setUserName();
}