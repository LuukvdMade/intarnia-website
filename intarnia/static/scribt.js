function openMenu()
{
    const nav = document.querySelector('nav');
    nav.classList.toggle('open');
}

const container = document.querySelector('.div-2');
const registerbutton = document.querySelector('.register header');
const loginbutton = document.querySelector('.login header');

loginbutton.addEventListener('click', () =>{
    container.classList.add('active');
})

registerbutton.addEventListener('click', () =>{
    container.classList.remove('active');
})

function closeflash() {
    const flashmessage = document.getElementById("flashmessage");
    flashmessage.remove();
  }