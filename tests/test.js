const login = (e)=>{
  e.preventDefault();
  const email = document.getElementById('login');
  const password = document.getElementById('password');
  axios.post('/login', {email, password}).then((response)=>{console.log(response)});
}
