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
    std::string data;
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

//int sendTelegramPhoto(string chat_id, string path_to_photo, string caption = NULL){
//    CURL *curl;
//    CURLcode response;
//    curl_global_init(CURL_GLOBAL_ALL);
//    curl = curl_easy_init();
//    if (curl)
//    {
//        curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);
//        curl_easy_setopt(curl, CURLOPT_POST, 1);
//        curl_easy_setopt(curl, CURLOPT_URL,     "https://api.telegram.org/bottoken/sendPhoto");
//        curl_easy_setopt(curl, CURLOPT_DEFAULT_PROTOCOL, "https");
//        struct curl_slist *headers = NULL;
//        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
//        curl_slist_append(headers, "Content-Type: multipart/form-data");
//        curl_slist_append(headers, "charset=utf-8");
//        curl_mime *mime;
//        curl_mimepart *part;
//        mime = curl_mime_init(curl);
//        part = curl_mime_addpart(mime);
//        curl_mime_name(part, "chat_id");
//        curl_mime_data(part, chat_id.c_str(), CURL_ZERO_TERMINATED);
//        part = curl_mime_addpart(mime);
//        curl_mime_name(part, "photo");
//        curl_mime_filedata(part, path_to_photo.c_str("example.jpg"));
//        curl_mime_type(part, "image/jpeg");
//        part = curl_mime_addpart(mime);
//        curl_mime_name(part, "caption");
//        curl_mime_data(part, caption.c_str().c_str(), CURL_ZERO_TERMINATED);
//        curl_easy_setopt(curl, CURLOPT_MIMEPOST, mime);
//        response = curl_easy_perform(curl);
//        curl_mime_free(mime);
//        curl_slist_free_all(headers);
//    }
//    curl_easy_cleanup(curl);
//    return 0;
//}

int main() {
    Bot bot("KEY_API_HERE");

    const string photoFilePath = "example.jpg";
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
