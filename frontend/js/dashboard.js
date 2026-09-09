const API='http://localhost:5000/api';
async function loadDashboard(){
  try{
    const [r,n,c,b]=await Promise.all([
      fetch(API+'/residents'),fetch(API+'/notices'),
      fetch(API+'/complaints'),fetch(API+'/bills')
    ]);
    document.getElementById('residentCount').textContent=(await r.json()).length;
    document.getElementById('noticeCount').textContent=(await n.json()).length;
    document.getElementById('complaintCount').textContent=(await c.json()).length;
    document.getElementById('billCount').textContent=(await b.json()).length;
  }catch(e){console.error(e)}
}
loadDashboard();
