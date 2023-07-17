async function make_request(url, context) {
    let response = await fetch(url, context);
    console.log(response)
    if (response.ok) {
        console.log('OK')
        return await response.json();
    } else {
        console.log('Not Successful')
        let error = new Error(response.statusText);
        error.response = response;
        error_res = await response.json();
        console.log(error_res.error)
        return error_res;
    }
}

// Getting CSRFToken
// let get_csrf_token = async function () {
//     let url = "item/receive_csrf_token/"
//     let request_csrf_token = await make_request(url, {method: "GET"});
// }


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// get_csrf_token();
// console.log(get_csrf_token());
let csrf_token = getCookie('csrftoken');


async function favorite(event) {
    event.preventDefault()
    let url = event.target.dataset.itemUrl;
    let data = await make_request(url, {
        method: "POST",
        headers: {"X-CSRFToken": csrf_token}
    });
    console.log(data.value);
    if (data.value === "Favourite"){
        event.target.innerText = data.value
    }else if (data.value === "Unfavorite"){
        event.target.innerText = data.value
    }
}


function onLoad() {

    const favouriteButtons = document.querySelectorAll(".favorite_button");
    favouriteButtons.forEach(function (fav) {
            fav.addEventListener('click', favorite)

        }
    )
}




window.onload = onLoad;



