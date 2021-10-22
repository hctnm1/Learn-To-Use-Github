const Discord = require('discord.js');
const translate = require('@vitalets/google-translate-api');
const {searchAll} = require('./middleware/paper')
require('dotenv').config();

const client = new Discord.Client();

client.login(process.env.DISCORD_BOT_TOKEN)

client.on('ready', () => {
    console.log('Crocs Bot Is Ready');
});

client.on('message', (msg) => {
    let command = msg.content.split(' ');
    if (command[0] === '#hello') msg.reply('hai');
    else if (command[0] === '#link'){
        const linkEmbed = new Discord.MessageEmbed()
            .setTitle('bot Link')
            .setAuthor('BOT')
        for (let i = 1; i < (command.length); i++) {
            linkEmbed.addFields([
                {name: `${command[i]}`, value:`[Link](https://wa.me/62${command[i].slice(1)})`}
            ])
        }
        msg.channel.send(linkEmbed);
    }else if(command[0] === '#translate'){
        let targetLang = command[1];
        let text = command.slice(2).join(' ');
        translate(text, {to: targetLang}).then((res)=>{
            const translateEmbed = new Discord.MessageEmbed()
                .setTitle('bot Translate')
                .setAuthor('BOT')
                .setDescription(`${res.text}`)
                .addFields([
                    {name: 'From', value: `${res.from.language.iso}`, inline: true},
                    {name: 'To', value: `${targetLang}`, inline: true},
                    {name: 'AutoCorrected', value: `${res.from.text.autoCorrected}`, inline: true},
                    {name: 'TextCorrected', value: `${res.from.text.autoCorrected?res.from.text.value:"Null"}`},
                ])
            msg.channel.send(translateEmbed);
        }).catch((err)=>{
            console.log(err)
        })
    }else if(command[0] === '#paper'){
        let page = command[1]
        let keyword = command.slice(2).join('%20');
        const paperEmbed = new Discord.MessageEmbed();
        searchAll(keyword, page).then(result =>{
            paperEmbed.setTitle('Bot Paper').setAuthor('BOT').setDescription(`Keyword : ${command.slice(2).join(" ")}`);
            for (const jurnal of result) {
                let url = jurnal.identifiers.pop().slice(4)
                console.log(url)
                paperEmbed.addFields([
                    {name: `${jurnal.title}`, value:`[Link to jurnal](${url})`}
                ])
            }
            msg.channel.send(paperEmbed);
        }).catch((err) => {
            console.log(err)
        })
    }else if(command[0] === '#help'){
        const helpEmbed = new Discord.MessageEmbed();
        helpEmbed.setTitle('manual of bot').setAuthor('BOT');
        helpEmbed.addFields([
            {name: `hello`, value:`#hello`},
            {name: `link`, value:`#link <nomor telpon>`},
            {name: `translate`, value:`#translate <kode bahasa> <teks>`},
            {name: `paper`, value:`#translate <halaman> <keyword>`},
            {name: `help`, value:`#help`},
        ])
        msg.channel.send(helpEmbed);
    }
});