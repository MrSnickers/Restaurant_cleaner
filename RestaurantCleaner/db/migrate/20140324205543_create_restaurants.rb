class CreateRestaurants < ActiveRecord::Migration
  def change
    create_table :restaurants do |t|
      t.string  :name
      t.string  :street_address
      t.integer :zip
      t.string  :cuisine
      t.string  :current_grade

      t.timestamps
    end
  end
end
