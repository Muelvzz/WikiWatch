import "./App.css";
import Home from "./pages/Home/Home";
import Navbar from "./pages/components/Navigation";
import api from './services/api'
import { useRef, useState, useEffect } from "react";

function App() {

  const inputRef = useRef(null)
  const [data, setData] = useState(null)

  const handleKeyDown = async (event) => {
      if (event.key === 'Enter') {
        
          try {
            const inputUrl = {
              url_input: inputRef.current.value
            }
            const response = await api.post( '/analyze', inputUrl)

            const urlData = response.data
            setData(urlData)
          } catch (err) {
            if (err.response?.status === 400) {
              console.log(err.response.data.detail)
            }
          }

        inputRef.current.value = ''; 
      }
    };

  useEffect(() => {
    if (data) {
      console.log(data)
    }
  }, [data])

  return (
    <>
      <Navbar 
        inputRef={inputRef}
        handleKeyDown={handleKeyDown}
      />
      <Home 
        inputRef={inputRef}
        handleKeyDown={handleKeyDown}
      />
    </>
  );
}

export default App;
