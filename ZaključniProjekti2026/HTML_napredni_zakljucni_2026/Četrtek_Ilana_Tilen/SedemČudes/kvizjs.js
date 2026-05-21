const vprasanja = [
	{
		vprasanje:"Kako se imenuje najstarejša in največja piramida v Gizi?",
		odgovori:[
			{besedilo:"Keopsova piramida",pravilen:true},
			{besedilo:"Kefrenova piramida",pravilen:false},
			{besedilo:"Mikerinova piramida",pravilen:false},
			{besedilo:"Rajeva piramida",pravilen:false},

		]
	},
	{
		vprasanje:"Koliko je Zevsov kip visok?",
		odgovori:[
			{besedilo:"21m",pravilen:false},
			{besedilo:"11m",pravilen:false},
			{besedilo:"19m",pravilen:false},
			{besedilo:"12m",pravilen:true},

		]
	},
    { 
        vprasanje:"Koliko stebrov je imel Mavzolej?",
        odgovori:[
            {besedilo:"43 stebrov.",pravilen:false},
            {besedilo:"67 stebrov.",pravilen:false},
            {besedilo:"27 stebrov.",pravilen:false},
            {besedilo:"36 stebrov.",pravilen:true},

        ]
    },
    {
        vprasanje:"Kdaj je skupina evropskih arhitektov napovedala načrte za izgradnjo sodobnega Kolosa?",
        odgovori:[
            {besedilo:"septembra 1999",pravilen:false},
            {besedilo:"decembra 2015",pravilen:true},
            {besedilo:"julija 2019",pravilen:false},
            {besedilo:"oktobra 2020",pravilen:false},

        ]
    },
    {
        vprasanje:"Kdaj se je začela gradnja Rodoškega kolosa?",
        odgovori:[
            {besedilo:"367 pr.n.št.",pravilen:false},
            {besedilo:"292 pr.n.št.",pravilen:true},
            {besedilo:"267 pr.n.št.",pravilen:false},
            {besedilo:"167 pr.n.št.",pravilen:false},

        ]
    },
    { 
        vprasanje:"Čemu so služile piramide v Egiptu?",
        odgovori:[
            {besedilo:"Služile so kot skladišče zlata.",pravilen:false},
            {besedilo:"Služile so kot domovi za kmete.",pravilen:false},
            {besedilo:"Služile so kot grobnice za faraone.",pravilen:true},
            {besedilo:"Služile so kot javno stranišče.",pravilen:false},

        ]
    },
    { 
        vprasanje:"Kje so zgrajeni Babilonski viseči vrtovi?",
        odgovori:[
            {besedilo:"V Sudanu.",pravilen:false},
            {besedilo:"Na Kitajskem.",pravilen:false},
            {besedilo:"V Ameriki.",pravilen:false},
            {besedilo:"Lokacija ni dokončno znana.",pravilen:true},

        ]
    },
    { 
        vprasanje:"Kdaj je Halikarnasi umrl?",
        odgovori:[
            {besedilo:"295 pr.n.št.",pravilen:false},
            {besedilo:"377 pr.n.št.",pravilen:true},
            {besedilo:"492 pr.n.št.",pravilen:false},
            {besedilo:"267 pr.n.št.",pravilen:false},

        ]
    },
    { 
        vprasanje:"Kdaj so naredili Zevsov kip v olimpiji?",
        odgovori:[
            {besedilo:"261 pr.n.št.",pravilen:false},
            {besedilo:"208 pr.n.št.",pravilen:false},
            {besedilo:"435 pr.n.št.",pravilen:true},
            {besedilo:"759 pr.n.št.",pravilen:false},

        ]
    },
    { 
        vprasanje:"Kje se nahaja Artemidin tempelj?",
        odgovori:[
            {besedilo:"Stal je v bližini starodavnega mesta Ofez.",pravilen:false},
            {besedilo:"Stal je v bližini starodavnega mesta Ifez.",pravilen:false},
            {besedilo:"Stal je v bližini starodavnega mesta Afez.",pravilen:false},
            {besedilo:"Stal je v bližini starodavnega mesta Efez.",pravilen:true},

        ]
    },
    { 
        vprasanje:"Kdo je ustvaril Babilonske viseče vrtove?",
        odgovori:[
            {besedilo:"Cesar Gaj Avgust Oktavijan.",pravilen:false},
            {besedilo:"Cesar Nebukadnezar II.",pravilen:true},
            {besedilo:"Cesar Honstantin Veliki.",pravilen:false},
            {besedilo:"Cesar Mark Avreelj IV.",pravilen:false},

        ]
    },
    { 
        vprasanje:"Koliko časa je trajala gradnja Aleksandrijskega svetilnika?",
        odgovori:[
            {besedilo:"Gradnja je trajala 53 let.",pravilen:false},
            {besedilo:"Gradnja je trajala 67 let.",pravilen:false},
            {besedilo:"Gradnja je trajala 12 let.",pravilen:true},
            {besedilo:"Gradnja se nikoli ni zaključila.",pravilen:false},

        ]
    },
    { 
        vprasanje:"Katerega leta so odkrili del mavzoleja?",
        odgovori:[
            {besedilo:"21 stoletja.",pravilen:false},
            {besedilo:"20 stoletja.",pravilen:false},
            {besedilo:"19 stoletja.",pravilen:true},
            {besedilo:"22 stoletja.",pravilen:false},

        ]
    },
    { 
        vprasanje:"Kdaj se je začela rekonstrukcija Artemidinega templja?",
        odgovori:[
            {besedilo:"183 pr. n. št.",pravilen:false},
            {besedilo:"650 pr. n. št.",pravilen:false},
            {besedilo:"550 pr. n. št.",pravilen:true},
            {besedilo:"391 pr. n. št.",pravilen:false},

        ]
    }




]

const vprasanjeElement= document.getElementById("vprasanje");
const odgovoriGumbi= document.getElementById("odgovori_btn");
const naslednjeGumb= document.getElementById("naslednje");
const sporocilo = document.getElementById("sporocilo");

let trenutnoIndeks = 0;
let tocke= 0;


function prikaziVprasanje() {
    let trenutnoVprasanje = vprasanja[trenutnoIndeks];

    vprasanjeElement.innerHTML = trenutnoVprasanje.vprasanje;
    odgovoriGumbi.style.pointerEvents = "auto";

    odgovoriGumbi.innerHTML = "";
    for (let i = 0; i < trenutnoVprasanje.odgovori.length; i++) {
    let odgovor= trenutnoVprasanje.odgovori[i];

    let gumb= document.createElement("button");
    gumb.innerText = odgovor.besedilo;
    gumb.classList.add("btn");
    preveri(odgovor, gumb);

    odgovoriGumbi.appendChild(gumb);
}


}




let prikazPravi = "";

function preveri(odg, btn) {
    if (odg.pravilen === true) {
        prikazPravi = odg.besedilo;
        btn.addEventListener("click", pravilnoPrikazi);
    } else {
        btn.addEventListener("click", napacnoPrikazi);
    }
}


function pravilnoPrikazi(event) {
    tocke++;
    event.target.style.backgroundColor = "green";
    sporocilo.innerText = "Odgovor je pravilen!";
    odgovoriGumbi.style.pointerEvents = "none";
}

function napacnoPrikazi(event) {
    event.target.style.backgroundColor = "red";
    sporocilo.innerText = "Napačno, pravilen odgovor je: " + prikazPravi;
    odgovoriGumbi.style.pointerEvents = "none";
}
					






naslednjeGumb.addEventListener("click", naslednje);

function naslednje() {
    trenutnoIndeks++;

    if (trenutnoIndeks < vprasanja.length) {
        prikaziVprasanje();
        sporocilo.innerText = "";
    } else {
        vprasanjeElement.innerHTML = "Konec kviza! Število pravilnih: " + tocke + "/" + vprasanja.length;
        odgovoriGumbi.innerHTML = "";
        naslednjeGumb.style.display = "none";
        sporocilo.innerText = "";
    }
}


prikaziVprasanje();
