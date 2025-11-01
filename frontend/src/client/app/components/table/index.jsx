import { Table } from 'antd';

const DataTable = ({ columns, data, rowKey }) => (
  <Table columns={columns} dataSource={data} rowKey={rowKey} />
);

export default DataTable;
