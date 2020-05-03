function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie !== '') {
 var cookies = document.cookie.split(';');
 for (var i = 0; i < cookies.length; i++) {
       var cookie = jQuery.trim(cookies[i]);
       if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
       }
 }
}
return cookieValue;
}

main.onclick = function(event){
event = event || window.event;           
let img = event.target.closest('.favorite');
console.log(img);
if (img){
 let apply=links[0];                          
 let cancl=links[1];
$.ajax(
    {
       url: '/add_favorite/',
       type: 'POST',
       dataType: 'json',
       data: {'query': "True", 'id': img.alt, csrfmiddlewaretoken: getCookie('csrftoken')},
       error: function () 
             {
                alert('Ошибка получения запроса')
             },
       success: function (data) 
          {
             console.log(data.result);
                         
             img.src=(!data.result)? (cancl): (apply);
          }
    });
}else{
let page = event.target.closest('.page');
if (page){
 let chield = page.querySelector('.title');
$.ajax(
    {
       url: '/add_history/',
       type: 'POST',
       dataType: 'json',
       data: {'id': chield.textContent, csrfmiddlewaretoken: getCookie('csrftoken')},
       error: function () 
             {
                alert('Ошибка получения запроса')
             },
       success: function (data) 
          {
             let container = document.getElementById('main');
             while (container.firstChild) {
                container.removeChild(container.firstChild);
             }
             let div = document.createElement('div');
             div.innerHTML = data.notifications_list
             container.appendChild(div);
             $(document).scrollTop(0);
          }
    });
}

}
}
let container = document.getElementById('main');
for (let i = 0; i!=container.children.length; i++)
{   
    let page = container.children[i];
    if(page.classList.contains('page'))
    {
        let image = page.querySelector('.favorite');
        $.ajax({
               url: '/add_favorite/',
               type: 'POST',
               dataType: 'json',
               data: {'query': "False", 'id': image.alt, csrfmiddlewaretoken: getCookie('csrftoken')},
               error: function () 
                     {
                        console.log('Ошибка получения запроса');
                     },
               success: function (data) 
                  {
                     console.log(data.result);
                        let apply=links[0];                          
                        let cancl=links[1];          
                     image.src=(data.result)? (apply):(cancl);
                  }
            });
      
    }
    
}
