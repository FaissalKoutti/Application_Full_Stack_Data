import { useState, useEffect } from "react";
import EarthquakeList from './EarthquakeList';

const BASE_URL = 'http://0.0.0.0:8002'
const KONG_ROUTE = '/api'
const BASE_ROUTE = BASE_URL + KONG_ROUTE

function FeedEarthquakes() {
  // State handling setup
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch(BASE_ROUTE + "/db/earthquakes/find")
      .then(res => res.json())
      .then(response => {
        setIsLoaded(true);
        setItems(response);
      })
      .catch((error) => {
        setIsLoaded(true);
        setError(error);
      });

  }, []);

  if (!isLoaded) {
    return (<p>Loading...</p>);
  } else if(error) {
    return (<p>Error: {error.message}</p>);
  } else {
    return (<EarthquakeList earthquakes={items}/>);
  }
}

export default FeedEarthquakes;