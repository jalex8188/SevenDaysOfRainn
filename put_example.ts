const myDataObject = {
    "id": 1,
    "Monday": false
};


const putData = async () => {
    const response = await fetch('http://localhost:3000/dwarves/1', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(myDataObject)
    });

    const data = await response.json();

    // now do whatever you want with the data  
    console.log(data);
};
putData();