export default class APIService{
    // Insert an article
    static InsertArticle(body){
        return fetch(`http://localhost:5000/add`,{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
            ('Access-Control-Allow-Origin: *')
            ('Access-Control-Allow-Headers: X-Requested-With')
            ("HTTP/1.1 200 OK")
      },
      body:JSON.stringify(body)
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }

}