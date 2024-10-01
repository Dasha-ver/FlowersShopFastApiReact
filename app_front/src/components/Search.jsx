import React from "react";

const Search = () => {
    const [searchTerm, setSearchTerm] = React.useState("");
    const [searchResults, setSearchResults] = React.useState([]);
    const handleChange = event => {
    setSearchTerm(event.target.value);
  };

    return(
        <div>
            <input class='input-search'
                type="text"
                placeholder="Поиск"
                value={searchTerm}
                onChange={handleChange}
              />
            </div>
)
}


export default Search;