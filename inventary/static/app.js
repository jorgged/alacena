const todoAdd = document.querySelectorAll(".add");
const todoDelete = document.querySelectorAll(".delete");
todoAdd.forEach((addbtn) => {
    const pk = addbtn.getAttribute("pk");
    addbtn.addEventListener("click", () => {
        addToShoppingCart(pk)
    });
})

todoDelete.forEach((deletebtn) => {
    const pk = deletebtn.getAttribute("pk");
    deletebtn.addEventListener("click", () => {
        QuitShoppingCart(pk)
    })
})

function addToShoppingCart(pk) {

    url = `/shoppingcart/add/${pk}/`
    fetch(url).then((res) => {
        console.log(res)
    }).catch((error) => {
        console.log(error.json())
    })
}

function QuitShoppingCart(pk) {
    const urlAbsolute = window.location.href
    const pathname = window.location.pathname

    const baseURL = urlAbsolute.replace(pathname, "")

    url = baseURL + `/shoppingcart/delete/${pk}/`
    fetch(url).then((res) => {
        console.log(res)
    }).catch((error) => {
        console.log(error)
    })
}