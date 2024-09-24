from parser.parser_for_links import ParserForLinks
from parser.parser_for_one_category import ParserForOneCategory

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/bukety-roz'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'bouquets_of_roses')

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/bukety-cvetov'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'bouquets')

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/cvety-v-korobke'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'flowers_boxes')

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/korziny-s-cvetami'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'flowers_baskets')

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/podarki/plyushevye-medvedi'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'toys')

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/vozdushnye-shary'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'balloons')

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/podarki'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'presents')

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/otkrytki'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'cards')

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/povod'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'celebrate')

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/komu'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'to_whom')

for item in ParserForLinks.get_links_by_link('https://dolinaroz.by/catalog/poshtuchno'):
    parser = ParserForOneCategory(item)
    ParserForOneCategory.run(parser, 'by_the_piece')







