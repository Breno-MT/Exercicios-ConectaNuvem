import Produto from "./classe.js"
import { calculaTotal } from "./func.js"


const arroz = new Produto('arroz', 3, 9);
const feijao = new Produto('feijao', 2, 12);
const batata = new Produto('batata', 4, 8);
const macarrao = new Produto('macarrao', 1, 5);
const total = calculaTotal(arroz, feijao, batata, macarrao)
console.log(total);