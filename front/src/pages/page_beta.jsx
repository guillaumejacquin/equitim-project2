import { useState } from 'react';
import Container from "@material-ui/core/Container";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import { FaPiedPiperAlt } from 'react-icons/fa';
import { FaInternetExplorer } from 'react-icons/fa';
import { ButtonGroup } from '@material-ui/core';
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import { FaJs } from 'react-icons/fa';
import { GiNotebook } from "react-icons/gi";
import { VscGraphLine } from "react-icons/vsc";
import { GiSpiralLollipop } from "react-icons/gi";
import { useModal } from 'react-hooks-use-modal';
import PreLoader2 from "../components/PreLoader2";
import PreLoader1 from "../components/preloader";


import DatePicker from '@mui/lab/DatePicker';
import InputLabel from '@mui/material/InputLabel';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';

import * as success from "../components/1127-success.json";


const menu_déroulant = (template, settemplate) => {
	const names = ['Test1', 'CSG', "crédit suisse", "test crédit suisse", "goldman sachs fci"]
  const dir = "../../../"
  //template bnp
  
  function importAll(r) {
    return r.keys().map(r);
  }
  
  const images = importAll(require.context('../../../Templates', true, /\.pptx/));
  
  console.log(images)
  return (
    <div>
    {/* <ul>{listItems}</ul> */}
   <Select
          labelId="template"
          id="template"
          value={template}
          label="template"
          onChange={(e)=>settemplate(e.target.value)}
          >
          
          {names.map(images => <MenuItem value={images}>{images}</MenuItem>)}


        </Select> 

    </div>
  );
}
const Page_beta = ({ formData, setForm, navigation }) => { 
  const premiertab = () => {
    return(
      <div style={{width: "20%", border: '1px solid grey', borderRadius:"4%", height:"5%", marginLeft:"10%"}}>
        <Container maxWidth="xs" style={{marginTop: "10%", marginBottom:"10%"}}>
          <h3 style={{textAlign:"center"}}> <GiNotebook/> Caractéristiques</h3>
          <TextField label="Nom du produit" name="Nom" 
          style={{marginTop:"8%"}}
            onChange={(e)=>setNom(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

        <InputLabel style={{marginTop:"5%" }}id="F0">Droit applicable</InputLabel>
        <Select
          labelId="Droit"
          id="Droit"
          value={Droit_applicable}
          label="Droit"
          onChange={(e)=>setDroit(e.target.value)}
          >
          <MenuItem value={"français"}>Français</MenuItem>
          <MenuItem value={"anglais"}>Anglais</MenuItem>
          <MenuItem value={"suisse"}>Suisse</MenuItem>
        </Select> 
            <TextField
            label="ISIN"
            name="Isin"
            onChange={(e)=>setISIN(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

            <div style={{marginTop:"8%"}}></div>

            <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Date d'émission"
                value={Emission}
                onChange={(Emission) => {
                  setEmission(Emission);
                  console.log(Emission)
                }}
                renderInput={(params) => <TextField {...params} />}
              />
              </LocalizationProvider>
              <div style={{marginTop:"8%"}}></div>
              <TextField
            label="Date(s) de constatation(s) initiale(s)"
            name="DCI"
            onChange={(e)=>setDCI(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>   <div style={{marginTop:"8%"}}></div>
            <LocalizationProvider dateAdapter={AdapterDateFns}>
            <DatePicker
              label="Date constatation 1er rappel "
              value={DPR}
              onChange={(DPR) => {
                setDPR(DPR);
              }}
              renderInput={(params) => <TextField {...params} />}
            />
          </LocalizationProvider>

              <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Date remboursement 1er rappel"
                value={DR1}
                onChange={(DR1) => {
                  setDR1(DR1);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>

            <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Avant dernière date de constatation"
                value={ADCF}
                onChange={(ADCF) => {
                  setADCF(ADCF);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>

            <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Avant dernière date de remboursement"
                value={DADR}
                onChange={(DADR) => {
                  setDADR(DADR);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>


            <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Date de constatation finale"
                value={DCF}
                onChange={(DCF) => {
                  setDCF(DCF);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>

            <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Date d'échéance"
                value={DEC}
                onChange={(DEC) => {
                  setDEC(DEC);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>

           

            <InputLabel style={{marginTop:"5%" }}id="F0">Template</InputLabel>
       
          
          {menu_déroulant(template, settemplate)}
      </Container>
    </div>
    )}

    const second_tab = () => {
      return(
        <div style={{width: "20%", height:"5%", border: '1px solid grey', borderRadius:"4%", marginLeft:"10%"}}>
        <Container maxWidth="xs" style={{marginTop: "10%", marginBottom:"10%"}}>
          <h3 style={{textAlign:"center"}}><VscGraphLine/> Pay-off</h3>
  
          <InputLabel style={{marginTop:"5%" }}id="F0">Typologie</InputLabel>
        <Select
          labelId="Typologie"
          id="Typologie"
          value={Typologie}
          label="Typologie"
          onChange={(e)=>setTypologie(e.target.value)}
          >
          <MenuItem value={"coupon autocall"}>Coupon Autocall</MenuItem>
          <MenuItem value={"coupon phoenix"}>Coupon Phoenix</MenuItem>


        </Select> 
      <InputLabel style={{marginTop:"5%" }}id="F0">Fréquence</InputLabel>
        <Select
          labelId="F0"
          id="F0"
          value={F0}
          label="F0"
          onChange={(e)=>setF0(e.target.value)}
          >
          <MenuItem value={"jours"}>Quotidienne</MenuItem>
          <MenuItem value={"mois"}>Mensuelle</MenuItem>
          <MenuItem value={"trimestre"}>Trimestrielle</MenuItem>
          <MenuItem value={"semestre"}>Semestrielle</MenuItem>
          <MenuItem value={"année"}>Annuelle</MenuItem>

        </Select>
        <InputLabel style={{marginTop:"5%" }}id="F0">Type de strike</InputLabel>
        <Select
          labelId="type_strike"
          id="type_strike"
          value={type_strike}
          label="type_strike"
          onChange={(e)=>settype_strike(e.target.value)}
          >
          <MenuItem value={"strike normal"}>Strike normal</MenuItem>
          <MenuItem value={"strike moyen"}>Strike moyen</MenuItem>
          <MenuItem value={"best strike"}>Best strike</MenuItem>

        </Select>


        <InputLabel style={{marginTop:"5%" }}id="F0">Type de barrière</InputLabel>
        <Select
          labelId="type_bar"
          id="type_bar"
          value={type_bar}
          label="type_bar"
          onChange={(e)=>settype_bar(e.target.value)}
          >
          <MenuItem value={"degressif"}>Dégressive</MenuItem>
          <MenuItem value={"airbag"}>Airbag</MenuItem>
          <MenuItem value={"normal"}>Normale</MenuItem>
        </Select> 


        <InputLabel style={{marginTop:"5%" }}id="F0">Type de sous jacent</InputLabel>
        <Select
          labelId="sous_jacent"
          id="sous_jacent"
          value={sous_jacent}
          label="sous_jacent"
          onChange={(e)=>setsous_jacent(e.target.value)}
          >
          <MenuItem value={"mono action"}>Mono action</MenuItem>
          <MenuItem value={"wo action"}>WO actions</MenuItem>
          <MenuItem value={"equipondéré action"}>Equipondéré actions</MenuItem>
          <MenuItem value={"mono indice"}>Mono indice</MenuItem>
          <MenuItem value={"equipondéré indice"}>Equipondéré indices</MenuItem>
          <MenuItem value={"wo indice"}>WO indices</MenuItem>

        </Select> 
        <TextField
            label="Sous-jacent(s)"
            name="TSJ"
            onChange={(e)=>setTSJ(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
      
        <TextField
            label="Coupon périodique (%)"
            name="CPN"
            onChange={(e)=>setCPN(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

  
        
    <InputLabel style={{marginTop:"5%" }}id="F0">Barrière coupon mémoire</InputLabel>
        <Select
          labelId="CPN_is_memoire"
          id="CPN_is_memoire"
          value={CPN_is_memoire}
          label="CPN_is_memoire"
          onChange={(e)=>setCPN_is_memoire(e.target.value)}
          >
          <MenuItem value={"oui"}>oui</MenuItem>
          <MenuItem value={"non"}>non</MenuItem>
        </Select>

      <TextField
            label="Niveau de barrière autocall (%)"
            name="BAC"
            onChange={(e)=>setBAC(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

         <TextField
            label="Niveau de barrière de coupon (%)"
            name="BCPN"
            onChange={(e)=>setBCPN(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

        <TextField
            label="Niveau de barrière de protection (%)"
            name="PDI"
            onChange={(e)=>setPDI(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
        
        <InputLabel style={{marginTop:"5%" }}id="F0">Barrière de remboursement anticipé dégressive</InputLabel>
        <Select
          labelId="BAC_is_degressif"
          id="BAC_is_degressif"
          value={BAC_is_degressif}
          label="BAC_is_degressif"
          onChange={(e)=>setBAC_is_degressif(e.target.value)}
          >
          <MenuItem value={"oui"}>oui</MenuItem>
          <MenuItem value={"non"}>non</MenuItem>
        </Select>
     
        <InputLabel style={{marginTop:"5%" }}id="F0">Typologie barrière autocall</InputLabel>
        <Select
          labelId="type_bar2"
          id="type_bar2"
          value={type_bar2}
          label="type_bar2"
          onChange={(e)=>settype_bar2(e.target.value)}
          >
          <MenuItem value={" "}>Aucune</MenuItem>
          <MenuItem value={"continue"}>Continue</MenuItem>
          <MenuItem value={"degressif"}>Dégressive</MenuItem>
          <MenuItem value={"airbag"}>Airbag</MenuItem>
        </Select>

        <div style={{marginTop:"8%"}}></div>

        <InputLabel style={{marginTop:"5%" }}id="F0">Barrière de coupon dégressive</InputLabel>
        <Select
          labelId="BCPN_is_degressif"
          id="BCPN_is_degressif"
          value={BCPN_is_degressif}
          label="BCPN_is_degressif"
          onChange={(e)=>setBCPN_is_degressif(e.target.value)}
          >
          <MenuItem value={"oui"}>oui</MenuItem>
          <MenuItem value={"non"}>non</MenuItem>
        </Select>
        <InputLabel style={{marginTop:"5%" }}id="F0">Début dégressivité Phoenix</InputLabel>

        <LocalizationProvider dateAdapter={AdapterDateFns}>
      <DatePicker
        label="Début dégressivité Phoenix"
        value={DDP}
        onChange={(DDP) => {
          setDDP(DDP);
        }}
        renderInput={(params) => <TextField {...params} />}
      />


      </LocalizationProvider>
        </Container>
        
        
      </div>
      )}

      const troisiemetab = () => {
        return(
          <div style={{width: "20%", height:"5%", border: '1px solid grey', borderRadius:"4%", marginLeft:"10%"}}>
          <Container maxWidth="xs" style={{marginTop: "10%", marginBottom:"10%"}}>
          <h3 style={{textAlign:"center"}}> <GiSpiralLollipop/> Divers</h3>
          
        
        <TextField
            label="Commission"
            name="COM"
            onChange={(e)=>setCOM(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

        <TextField
            label="Niveau de scénario défavorable (%)"
            name="NSD"
            onChange={(e)=>setNSD(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />
        <TextField
            label="Niveau de scénario médian (%)"
            name="NSM"
            onChange={(e)=>setNSM(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

        <TextField
            label="Niveau de scénario favorable (%)"
            name="NSF"
            onChange={(e)=>setNSF(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

        <TextField
            label="Avant dernier niveau de barrière autocall (%)"
            name="ABDAC"
            onChange={(e)=>setABDAC(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

        <TextField
            label="Dernier niveau de barrière gains/coupons (%)"
            name="DBAC"
            onChange={(e)=>setDBAC(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />
        <TextField
            label="Pas de degressivité (%)"
            name="DEG"
            onChange={(e)=>setDEG(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

          <TextField
            label="Nombre de jours ouvrés"
            name="NJO"
            onChange={(e)=>setNJO(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

     

        
        
        </Container>
        </div>
          )}
          
  const handleSubmit  = (event) => {
      event.preventDefault();

    // Simple POST request with a JSON body using fetch
    
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          Nom: Nom, Typologie:Typologie,
          Droit: Droit_applicable, Isin: Isin, Emission:Emission, DCI:DCI,
          DR1:DR1, DPR:DPR, DADR:DADR, DCF:DCF, DEC:DEC, ADCF:ADCF,
          F0:F0, TSJ:TSJ, PCS1:PCS1, PCS2:PCS2, PCS3:PCS3, PCS4:PCS4, PCS5:PCS5,
          CPN:CPN, CPN_is_memoire:CPN_is_memoire, PDI:PDI, 
          BAC:BAC, BAC_is_degressif:BAC_is_degressif, BCPN:BCPN, BCPN_is_degressif:BCPN_is_degressif,
           COM:COM, NSD:NSD, NSM:NSM, NSF:NSF,
          ABDAC:ABDAC, DBAC:DBAC, DEG:DEG, type_strike:type_strike,
          type_bar:type_bar, sous_jacent:sous_jacent, template:template, DDP:DDP, type_bar2:type_bar2, NJO:NJO 
        })
    };
    // setLoading(true);
    let test = ""
    fetch('http://localhost:5000/add', requestOptions)
        .then(response => response.json())
        .then(response => setResponse(response))
        .then(response =>     console.log(requestOptions)        )

        .then(response => test = (response))

        .catch(error => console.log(error))


      }


  const [Nom, setNom] = useState('')
  const [Typologie, setTypologie] = useState('')
  const [Droit_applicable, setDroit] = useState('')
  const [Isin, setISIN] = useState('')
  const [Emission, setEmission] = useState('')
  const [DCI, setDCI] = useState('')
  const [DR1, setDR1] = useState('')
  const [DPR, setDPR] = useState('')
  const [DADR, setDADR] = useState('')
  const [DCF, setDCF] = useState('')
  const [DEC, setDEC] = useState('')
  const [ADCF, setADCF] = useState('')
  const [F0, setF0] = useState('')
  const [TSJ, setTSJ] = useState('')
  const [DDP, setDDP] = useState('')

  const [PCS1, setPCS1] = useState('')
  const [PCS2, setPCS2] = useState('')
  const [PCS3, setPCS3] = useState('')
  const [PCS4, setPCS4] = useState('')
  const [PCS5, setPCS5] = useState('')

  
  const [CPN, setCPN] = useState('')
  const [CPN_is_memoire, setCPN_is_memoire] = useState('')
  const [PDI, setPDI] = useState('')
  const [BAC, setBAC] = useState('')
  const [BAC_is_degressif, setBAC_is_degressif] = useState('')
  const [BCPN, setBCPN] = useState('')
  const [BCPN_is_degressif, setBCPN_is_degressif] = useState('')

  const [COM, setCOM] = useState('')
  const [NSD, setNSD] = useState('')
  const [NSM, setNSM] = useState('')
  const [NSF, setNSF] = useState('')
  const [ABDAC, setABDAC] = useState('')
  const [DBAC, setDBAC] = useState('')
  const [DEG, setDEG] = useState('')
  const [type_strike, settype_strike] = useState('')
  const [type_bar, settype_bar] = useState('')
  const [sous_jacent, setsous_jacent] = useState('')
  const [template, settemplate] = useState('')
  const [type_bar2, settype_bar2 ] = useState('')
  const [loading, setLoading] = useState(false)

  const [response, setResponse] = useState("")
  const [NJO, setNJO] = useState("")

  const [Modal, open, close, isOpen] = useModal('root', {
    preventScroll: true,
    closeOnOverlayClick: false
  });
      //{blabla()}

  const blabla = () => {
    // if (response == "True") {
    //   return(
    //     //<PreLoader1/>
    //   )
    // }
    console.log("i")
  }
  const props = { formData, navigation};

  const a = [];

  const defaultOptions2 = {
    loop: true,
    autoplay: true,
    animationData: success.default,
    rendererSettings: {
      preserveAspectRatio: "xMidYMid slice",
    },
  };

return (
  <div style={{height: "100%"}}>
    <div>
        <h1 style={{textAlign:"center", marginTop:"1%"}}>Formulaire</h1>

    </div>
    <div style={{display: "flex", marginTop:"10%"}}>
      {(loading)
          ? <div style={{backgroundColor:"red"}}> <PreLoader2 /> </div>
          : <div style={{ textAlign:"center"}}>
          </div>
        }
      {blabla()}

      {premiertab()}
      {second_tab()}
      {troisiemetab()}
    </div>
          <Button
          variant="contained"
            color="primary"
            size="large"
            style={{ marginTop: "6%", left:"40%", width:"20%"}}
            onClick={handleSubmit}
          >
            Next
          </Button>

  </div>
);
  
}

export default Page_beta;


