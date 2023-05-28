UPDATE {tableName}
SET {columnName} = :newValue, LastModifiedBy = :lastModifiedBy, LastModifiedOn = getDate()
WHERE {primaryKey} = :primaryKeyValue