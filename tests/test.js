const login = (e)=>{
  e.preventDefault();
  const email = document.getElementById('login');
  const password = document.getElementById('password');
  axios.post('/login', {email, password}).then((response)=>{console.log(response.data)});
}

const signUp = ()=>{
  const user = {
    cin: document.getElementById('cin').value,
    socialReason: document.getElementById('socialReason').value,
    revenueStamp: document.getElementById('revenueStamp').value,
    login: document.getElementById('login').value,
    password: document.getElementById('password').value,
    address: [{
      country: document.getElementById('country').value,
      cityOrVillage: document.getElementById('cityOrVillage').value,
      zipCode: document.getElementById('zipCode').value,
    }],
    phones: [
      document.getElementById('phone1').value,
      document.getElementById('phone2').value,
      document.getElementById('phone3').value
    ],
    emails:[login],
    roles:[],
    active: true,
  };
  axios.post('http://localhost:5000/signUp',{request: 'signup', 'user': user},
  {headers: {'Content-Type': 'application/json','Access-Control-Allow-Origin': '*'}
}).then(response => {console.log(response.data)}).catch(
    error => console.log(error.message)
  );
}
