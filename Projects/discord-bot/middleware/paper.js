const axios = require('axios');

let api_key = process.env.CORE_API_KEY;

const searchAll = async (keyword, page) => {
    let result = []
    page = page ? page : '1'
    let url = `https://core.ac.uk:443/api-v2/journals/search/${keyword}?page=${page}&pageSize=100&apiKey=${process.env.CORE_API_KEY}`
    let res = await axios.get(url)
    result = [...res.data.data];
    return result;
}

module.exports = {
    searchAll
}
