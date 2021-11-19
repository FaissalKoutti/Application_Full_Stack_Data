import { useState, useEffect } from "react";

// Constants
const FILTER_MAG = 6.0;
const BASE_URL = 'http://0.0.0.0:8002'
const KONG_ROUTE = '/api'
const BASE_ROUTE = BASE_URL + KONG_ROUTE

function getColor(agg_type) {
    if (agg_type == 'count') return 'success';
    else if (agg_type == 'avg') return 'info';
    else if (agg_type == 'max') return 'danger';
    else if (agg_type == 'filter') return 'warning';
    else return 'light';
}

function getUrl(agg_type) {
    if (agg_type == 'count') 
        return BASE_ROUTE + '/db/earthquakes/count';
    else if (agg_type == 'filter') 
        return BASE_ROUTE + '/db/earthquakes/count?min_magnitude=' + FILTER_MAG;
    else 
        return BASE_ROUTE + '/db/earthquakes/aggregation?type_agg=' + agg_type;
}

function getValue(response, agg_type) {
    if (agg_type === 'count' || agg_type === 'filter') 
        return response['count'];
    else {
        if(response['value'].length === 0) return 'No data'

        return parseFloat(response['value'][0][agg_type]).toFixed(2);
    }
}

function MetricFeed(agg_type) {
    // State handling setup
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [value, setValue] = useState('...');

    // State behaviour
    useEffect(() => {
        fetch(getUrl(agg_type))
            .then(res => res.json())
            .then(response => {
                setValue(response);
                setIsLoaded(true);
            })
            .catch((error) => {
                setIsLoaded(true);
                setError(error);
            });

    }, []);

    if (!isLoaded)
        return (<div class="spinner-border spinner-border-sm" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>);
    else if (error)
        return "ERROR: " + error.message;
    else
        return getValue(value, agg_type);
}

function MetricCard({ description, agg_type }) {
    // Style setup
    const cardBg = "card bg-" + getColor(agg_type) + " mb-3 shadow-sm"

    return (
        <div className={cardBg} style={{ 'max-width': "18rem" }}>
            <div className="card-body font-weight-bold text-white">
                <h5 className="card-title text-white">{MetricFeed(agg_type)}</h5>
                <h6>{description}</h6>
            </div>
        </div>
    );
}

export default MetricCard;