const checkImage = path =>
new Promise(resolve => {
 const img = new Image();
 img.onload = () => resolve({
    path,
    status: 'ok'
 });
 img.src = path;
}).then(result => console.log(result.status, '...image is loaded from', path));

const loadImg = (paths) => Promise.all(paths.map(checkImage)).then(results => console.log('...all images are loaded'));


loadImg(links);