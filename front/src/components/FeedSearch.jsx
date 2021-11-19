import { useState, useEffect } from "react";
import EarthquakeList from './EarthquakeList';

const BASE_URL = 'http://0.0.0.0:8002'
const KONG_ROUTE = '/api'
const BASE_ROUTE = BASE_URL + KONG_ROUTE
const MAX_LIMIT = 50

function FeedSearch({min_magnitude, max_magnitude, tsunami}) {
    // Query parameters
    var parameters = "?limit=" + String(MAX_LIMIT)

    if(min_magnitude)
        parameters += "&min_magnitude=" + String(min_magnitude) + "&"
    if(max_magnitude)
        parameters += "&max_magnitude=" + String(max_magnitude) + "&"
    if(tsunami)
        parameters += "&tsunami=" + String(tsunami) + "&"

    // State handling setup
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetch(BASE_ROUTE + "/db/earthquakes/find" + parameters)
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
        return (<></>);
    } else if (error) {
        return (<p>Error: {error.message}</p>);
    } else {
        return (<EarthquakeList earthquakes={items} />);
    }
}

export default FeedSearch;