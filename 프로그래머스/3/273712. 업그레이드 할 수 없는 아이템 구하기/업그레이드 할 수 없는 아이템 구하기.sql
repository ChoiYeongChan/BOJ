SELECT I.ITEM_ID as ITEM_ID, I.ITEM_NAME as ITEM_NAME, I.RARITY as RARITY
FROM ITEM_INFO I JOIN ITEM_TREE T ON  I.ITEM_ID=T.ITEM_ID
WHERE I.ITEM_ID not in (
    SELECT PARENT_ITEM_ID
    FROM ITEM_TREE
    WHERE PARENT_ITEM_ID is not NULL
)
ORDER BY ITEM_ID DESC