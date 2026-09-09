const API='http://localhost:5000/api';
async function loadBills(){
 const data=await (await fetch(API+'/bills')).json();
 document.getElementById('billList').innerHTML=data.map(x=>`<div class="item"><h3>${x.resident} - Flat ${x.flat}</h3><p>Amount: ₹${x.amount}</p><p>Status: ${x.status}</p></div>`).join('');
}
loadBills();
