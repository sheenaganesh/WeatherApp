<script>
    async function fetchDataFromApi(location){
    const res = await fetch("http://127.0.0.1:8000/" + location)
    return await res.json()
	}

    let data = fetchDataFromApi("London")

    async function dropDownChange(e) {
        data = fetchDataFromApi(e.target.value);
    }
</script>

<h1>Weather app</h1>
<h1>current weather</h1>
<select on:change={dropDownChange}> 
    <option value="London">London</option>
    <option value="New York">New York</option>
    <option value="Paris">Paris</option>
</select>

{#await data}
    <p>Fetching</p>
{:then data}
    <p>Temperature is {data.Temperature}</p>
    <p>Weather is {data.Weather}</p>
{/await}