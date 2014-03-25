class CreateInspections < ActiveRecord::Migration
  def change
    create_table :inspections do |t|
      t.datetime :inspection_date
      t.string  :violation
      t.integer :restaurant_id

      t.timestamps
    end
  end
end
