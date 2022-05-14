//BIG THX: https://youtu.be/dwij9ZytWbQ
//         https://www.youtube.com/channel/UCu60M9W_SX-SNo53CDNVJ4w
//         https://github.com/reo7sp/tgbot-cpp
//         https://stackoverflow.com/questions/36702888/download-an-image-from-an-url-using-curl-in-c
//         https://stackoverflow.com/questions/36693792/text-parser-c-code#36696232
//         https://stackoverflow.com/questions/46261431/parsing-through-text-file-with-c
//         https://stackoverflow.com/questions/9551014/reading-parsing-text-file-input-c
//         https://www.cplusplus.com/forum/beginner/879/
#include <iostream>
#include <stdio.h>
#include <tgbot/tgbot.h>
#include <vector>
#include <ctime>
#include <csignal>
#include <cstdio>
#include <cstdlib>
#include <exception>
#include <string>
#include <nlohmann/json.hpp>
#include <curl/curl.h>

//https://thiscatdoesnotexist.com/
using namespace std;
using namespace TgBot;

vector<string> bot_commands= {"start", "echo", "time", "currency", "random_picture"};

static char errrorBuffer[CURL_ERROR_SIZE];
static string buffer;

static int Writer(char *buffer, size_t size, size_t nmemb, string *html)
{
    int result=0;

    if (buffer != NULL)
    {
        html -> append(buffer, size*nmemb);
        result = size*nmemb;
    }
}

string get_request(string link)
{
    CURL *curl;
    string data;
    curl=curl_easy_init();
    curl_easy_setopt(curl, CURLOPT_URL, link.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, Writer);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &data);
    curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    return data;
}

float get_currency(char what)
{
    auto js_obj = nlohmann::json::parse(get_request("https://www.cbr-xml-daily.ru/daily_json.js"));

    if (what=='u'){
        return js_obj["Valute"]["USD"]["Value"].get<float>();
    }
    else{
        return js_obj["Valute"]["KZT"]["Value"].get<float>();
    }
    return -1;
}

string get_time_as_str()
{
    time_t now = time(NULL);
    tm* ptr = localtime(&now);
    char buf[32];
    strftime(buf, 32, "%c", ptr);
    return buf;
}


size_t callbackfunction(void *ptr, size_t size, size_t nmemb, void* userdata)
{
    FILE* stream = (FILE*)userdata;
    if (!stream)
    {
        printf("!!! No stream\n");
        return 0;
    }

    size_t written = fwrite((FILE*)ptr, size, nmemb, stream);
    return written;
}

bool download_jpeg(char* url)
{
    FILE* fp = fopen("out.jpg", "wb");
    if (!fp)
    {
        printf("!!! Failed to create file on the disk\n");
        return false;
    }

    CURL* curlCtx = curl_easy_init();
    curl_easy_setopt(curlCtx, CURLOPT_URL, url);
    curl_easy_setopt(curlCtx, CURLOPT_WRITEDATA, fp);
    curl_easy_setopt(curlCtx, CURLOPT_WRITEFUNCTION, callbackfunction);
    curl_easy_setopt(curlCtx, CURLOPT_FOLLOWLOCATION, 1);

    CURLcode rc = curl_easy_perform(curlCtx);
    if (rc)
    {
        printf("!!! Failed to download: %s\n", url);
        return false;
    }

    long res_code = 0;
    curl_easy_getinfo(curlCtx, CURLINFO_RESPONSE_CODE, &res_code);
    if (!((res_code == 200 || res_code == 201) && rc != CURLE_ABORTED_BY_CALLBACK))
    {
        printf("!!! Response code: %d\n", res_code);
        return false;
    }

    curl_easy_cleanup(curlCtx);

    fclose(fp);

    return true;
}

int main()
{
    Bot bot("KEY API HERE..or token");

    const string photoFilePath = "out.jpg";
    const string photoMimeType = "image/jpeg";

    InlineKeyboardMarkup::Ptr keyboard(new InlineKeyboardMarkup);
    vector<InlineKeyboardButton::Ptr> row0;
    InlineKeyboardButton::Ptr usd_btn(new InlineKeyboardButton), kazah_peso(new InlineKeyboardButton);
    usd_btn -> text = "USD";
    usd_btn->callbackData = "USD";
    kazah_peso -> text = "Kazah_peso";
    kazah_peso -> callbackData = "Kazahstan Peso";
    row0.push_back(usd_btn);
    row0.push_back(kazah_peso);
    keyboard->inlineKeyboard.push_back(row0);

    bot.getEvents().onCommand("start", [&bot](Message::Ptr message) 
    {
        bot.getApi().sendMessage(message->chat->id, "Wake up "+ message->chat->firstName);
    });

    bot.getEvents().onCommand("time", [&bot](Message::Ptr message) 
    {
        bot.getApi().sendMessage(message->chat->id, "MSC time: "+get_time_as_str());
    });

    bot.getEvents().onCommand("currency", [&bot,&keyboard](Message::Ptr message) 
    {
        bot.getApi().sendMessage(message->chat->id, "How currency?", false, 0, keyboard);
    });

    bot.getEvents().onCommand("random_picture", [&bot, &photoFilePath, &photoMimeType](Message::Ptr message) {
        bot.getApi().sendPhoto(message->chat->id, InputFile::fromFile(photoFilePath, photoMimeType));
        download_jpeg("https://thiscatdoesnotexist.com/");
    });

    bot.getEvents().onCallbackQuery([&bot, &keyboard](CallbackQuery::Ptr query) {
        if (query->data == "USD") 
        {
            bot.getApi().sendMessage(query->message->chat->id, to_string(get_currency('u')));
        }
        else
        {
            bot.getApi().sendMessage(query->message->chat->id, to_string(get_currency('k')));
        }
    });

    bot.getEvents().onAnyMessage([&bot](Message::Ptr message)
    {
        for(const auto& command : bot_commands)
        {
            if ("/"+command==message->text)
            return;
        }
        bot.getApi().sendMessage(message->chat->id, "Your message is: " + message->text + ". And isn't a command owo");
    });

    try {
        printf("Bot username: %s\n", bot.getApi().getMe()->username.c_str());
        TgLongPoll longPoll(bot);
        while (true)
        {
            printf("Long poll started\n");
            longPoll.start();
        }
    }
    catch (TgException& e)
    {
        printf("error: %s\n", e.what());
    }
    return 0;
}




//=================================================================
//    <one line to give the program's name and a brief idea of what it does.>
//    Copyright (C) <year>  <name of author>
//
//    This program is free software: you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with this program.  If not, see <https://www.gnu.org/licenses/>.
