import { useState } from 'react';
import Container from "@material-ui/core/Container";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import { FaPiedPiperAlt } from 'react-icons/fa';
import { FaInternetExplorer } from 'react-icons/fa';
import { ButtonGroup } from '@material-ui/core';
import { FaJs } from 'react-icons/fa';
import Page2 from "../pages/page2";

const Page1 = ({ formData, setForm, navigation }) => { 
  const { go } = navigation;

  const { firstName, lastName, nickName } = formData;

  const premiertab = () => {
    return(
      <div style={{width: "20%", border: '1px solid grey', borderRadius:"4%", height:"5%", marginLeft:"10%"}}>
        <Container maxWidth="xs" style={{marginTop: "10%", marginBottom:"10%"}}>
          <h3 style={{textAlign:"center"}}> <FaPiedPiperAlt/> Premier Bloc</h3>
          <TextField label="Nom" name="Nom" 
          style={{marginTop:"8%"}}
            onChange={(e)=>setNom(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
          <TextField
            label="Droit"
            name="Droit"
            onChange={(e)=>setDroit(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="off"
            fullWidth/>

            <TextField
            label="Droit"
            name="Droit"
            onChange={(e)=>setDroit(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="off"
            fullWidth/>

            <TextField
            label="Droit"
            name="Droit"
            onChange={(e)=>setDroit(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="off"
            fullWidth/>

      </Container>
    </div>
    )}

    const second_tab = () => {
      return(
        <div style={{width: "20%", height:"5%", border: '1px solid grey', borderRadius:"4%", marginLeft:"10%"}}>
        <Container maxWidth="xs" style={{marginTop: "10%", marginBottom:"10%"}}>
          <h3 style={{textAlign:"center"}}><FaInternetExplorer/> Second Bloc</h3>
          <TextField style={{marginTop:"8%"}}

            label="Nom"
            name="Nom"
            onChange={(e)=>setNom(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
          <TextField
            label="Droit"
            name="Droit"
            onChange={(e)=>setDroit(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="off"
            fullWidth/>
        </Container>
      </div>
      )}

 
  const handleSubmit  = (event) => {
      event.preventDefault();

    // Simple POST request with a JSON body using fetch
    
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: Nom })
    };
    
    fetch('http://localhost:5000/add', requestOptions)
        .then(response => response.json())
        .catch(error => console.log(error)) 
  }




  const [Nom, setNom] = useState('')
  const [Droit_applicable, setDroit] = useState('')
  const props = { formData, navigation};


return (
  <div style={{height: "100%"}}>
    <div>
    <ButtonGroup variant="outlined" aria-label="outlined button group" size="large" style={{marginLeft:"20%"}}>
      <Button  style={{maxWidth: '100px', maxHeight: '100px', minWidth: '200PX', minHeight: '100px'}} > UN               </Button>
      <Button onClick={() => navigation.go("Page2")} style={{maxWidth: '100px', maxHeight: '100px', minWidth: '200PX', minHeight: '100px'}} > DEUX</Button>
      <Button style={{maxWidth: '100px', maxHeight: '100px', minWidth: '200PX', minHeight: '100px'}}> TROIS </Button>
    </ButtonGroup>

    </div>
    <div style={{display: "flex", marginTop:"10%"}}>
      {premiertab()}
      {second_tab()}

      <div style={{width: "20%", height:"5%", border: '1px solid grey', borderRadius:"4%", marginLeft:"10%"}}>
        <Container maxWidth="xs" style={{marginTop: "10%", marginBottom:"10%"}}>
          <h3 style={{textAlign:"center"}}> <FaJs/> Troisieme bloc</h3>
          <TextField label="Nom" name="Nom"
            style={{marginTop:"8%"}}

            onChange={(e)=>setNom(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />
          
          <TextField
            label="Droit"
            name="Droit"
            onChange={(e)=>setDroit(e.target.value)}

            margin="normal"
            variant="outlined"
            autoComplete="off"
            fullWidth
          />
        </Container>
      </div>
    </div>
          <Button
          variant="contained"
            
            color="primary"
            size="large"
            style={{ marginTop: "8%", left:"40%", width:"20%"}}
            onClick={handleSubmit}

          >
            Next
          </Button>

  </div>
);
  
}

export default Page1;


