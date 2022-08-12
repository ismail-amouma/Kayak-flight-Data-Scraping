from code import *
import code as  bot
def main():
    city_from = str(input('From which city?: '))
    city_to = str(input('Where to?: '))
    date_start = str(input('when u will flight? use DD-MM-YYYY: '))
    date_end = input('when will you return? use DD-MM-YYYY: ')
    bot.set_up_driver()
    bot.first_page()
    bot.place(city_from,city_to)
    bot.set_date(date_start,date_end)
    bot.search()
    bot.kayak_scraping(city_from,city_to,date_start,date_end)
if __name__ == "__main__":
    main()