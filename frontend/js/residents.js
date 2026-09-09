const API='http://localhost:5000/api';
async function loadResidents(){
 const data=await (await fetch(API+'/residents')).json();
 document.getElementById('residentList').innerHTML=data.map(x=>`<div class="item"><h3>${x.name}</h3><p>Flat: ${x.flat}</p><p>${x.phone||''} ${x.email||''}</p></div>`).join('');
}
document.getElementById('residentForm').addEventListener('submit',async e=>{
 e.preventDefault();
 await fetch(API+'/residents',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({
  name:name.value,flat:flat.value,phone:phone.value,email:email.value
 })});
 e.target.reset(); loadResidents();
});
loadResidents();
