const API='http://localhost:5000/api';
async function loadNotices(){
 const data=await (await fetch(API+'/notices')).json();
 document.getElementById('noticeList').innerHTML=data.map(x=>`<div class="item"><h3>${x.title}</h3><p>${x.message}</p><p class="muted">${x.date}</p></div>`).join('');
}
loadNotices();
