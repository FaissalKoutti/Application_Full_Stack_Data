// Search.jsx
import { useState, useEffect } from 'react';
import React, { Component } from 'react';
import FeedSearch from './FeedSearch';

function Search() {
    const [content, setContent] = useState(<></>);

    const handleSubmit = (event) => {
        event.preventDefault();
        setContent(<></>);
        const data = new FormData(event.target);
        setContent(<FeedSearch min_magnitude={data.get('min-magnitude')} 
                max_magnitude={data.get('max-magnitude')} tsunami={data.get('tsunami')}/>);
        
    }

    const clearResults = (event) => {
        setContent(<p></p>);
    };

    return (
        <div className="container">
            <h3>Search</h3>
            <div className="container card">
                <form className="card-body" onSubmit={handleSubmit}>
                    <label for="min-magnitude" className="form-label">Minimum magnitude</label>
                    <input type="number" className="form-control" name="min-magnitude" id="min-magnitude" />
                    <br />

                    <label for="max-magnitude" className="form-label">Maximum magnitude</label>
                    <input type="number" className="form-control" name="max-magnitude" id="max-magnitude" />
                    <br />

                    <div class="form-check form-switch">
                        <input className="form-check-input" type="checkbox" role="switch" name="tsunami" id="tsunami" />
                        <label className="form-check-label" for="tsunami">Provoked a tsunami</label>
                    </div>
                    <br />

                    <input type="submit" className="btn-check" id="submit" autocomplete="off" />
                    <label className="btn btn-primary" for="submit">Submit</label>

                    <br /><br />
                    <button type="button" onClick={clearResults} className="btn btn-danger">Clear</button>
                </form>
            </div>

            <hr />

            <h4>Results</h4>
            {content}
        </div>
    );
}


export default Search;